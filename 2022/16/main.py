import re

FILENAME = "input.txt"


def parse_input():
    nodes = {}
    edges = {}
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            match = re.search(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)", line)
            valve = match.group(1)
            flow = int(match.group(2))
            nodes[valve] = flow
            edges[valve] = set()
            for end in match.group(3).split(", "):
                edges[valve].add(end)
    return nodes, edges


def distance(edges, start, end):
    buffer = [(start, 0)]
    seen = set()
    while len(buffer) > 0:
        u, d = buffer.pop(0)
        if u == end:
            return d
        if u in seen:
            continue
        seen.add(u)
        for v in edges[u]:
            buffer.append((v, d + 1))


def part_one():
    nodes, edges = parse_input()

    # distances = {}
    # for u in nodes:
    #     distances[u] = {}
    #     for v in nodes:
    #         distances[u][v] = distance(edges, u, v)

    paths = {}
    for u in nodes:
        paths[u] = {}
        
        buffer = [u]
        seen = set()
        parents = {u: None}
        while len(buffer) > 0:
            k = buffer.pop(0)
            if k in seen:
                continue
            seen.add(k)
            for v in edges[k]:
                if v not in parents:
                    parents[v] = k
                buffer.append(v)
        for v in nodes:
            paths[u][v] = [v]
            w = v
            while w != u and w is not None:
                w = parents[w]
                paths[u][v].insert(0, w)

    distances = {}
    for u in nodes:
        distances[u] = {}
        for v in nodes:
            distances[u][v] = len(paths[u][v]) - 1

    # distances = {}
    # for u in nodes:
    #     distances[u] = {}
    #     for v in nodes:
    #         distances[u][v] = distance(edges, u, v)  
    
    state = ("AA", 0, set([u for u in nodes if nodes[u] > 0]), 0, 0)
    buffer = [state]
    max_total = 0
    time_of_max_total = 0

    while len(buffer) > 0:
        u, time, closed, rate, total = buffer.pop(0)
        if time > 30:
            continue
        total_at_30 = (30 - time) * rate + total
        if total_at_30 > max_total:
            max_total = total_at_30
            time_of_max_total = time
        for v in closed:
            if time + distances[u][v] + 1 > 30:
                continue
            buffer.append((
                v,
                time + distances[u][v] + 1,
                closed.difference([v]),
                rate + nodes[v],
                total + rate * (distances[u][v] + 1)
            ))
    print(time_of_max_total)
    return max_total



def part_two():
    
    nodes, edges = parse_input()

    paths = {}
    for u in nodes:
        paths[u] = {}
        
        buffer = [u]
        seen = set()
        parents = {u: None}
        while len(buffer) > 0:
            k = buffer.pop(0)
            if k in seen:
                continue
            seen.add(k)
            for v in edges[k]:
                if v not in parents:
                    parents[v] = k
                buffer.append(v)
        for v in nodes:
            paths[u][v] = [v]
            w = v
            while w != u and w is not None:
                w = parents[w]
                paths[u][v].insert(0, w)

    distances = {}
    for u in nodes:
        distances[u] = {}
        for v in nodes:
            distances[u][v] = len(paths[u][v]) - 1

    
    state = ("AA", None, "AA", None, 0, frozenset([u for u in nodes if nodes[u] > 0]), 0, 0)
    buffer = [state]
    max_total = 0

    i = 0

    while len(buffer) > 0:
        i += 1

        if i == 1000:
            print("\r", len(buffer), max_total, "    ", end="", flush=True)
            i = 0

        state = buffer.pop(0)
        u_me, g_me, u_elephant, g_el, time, closed, rate, total = state

        if time > 26:
            continue
        total_at_30 = (26 - time) * rate + total
        if total_at_30 > max_total:
            max_total = total_at_30
            
        closed_me = closed
        if g_me is not None:
            closed_me = [g_me]

        closed_el = closed
        if g_el is not None:
            closed_el = [g_el]

        if len(closed_me) == 1 and len(closed_el) == 1 and list(closed_me)[0] == list(closed_el)[0]:
            v_me = list(closed_me)[0]
            v_elephant = list(closed_el)[0]
            if distances[u_elephant][v_elephant] <= distances[u_me][v_me]:
                buffer.append((
                    None,
                    None,
                    v_elephant,
                    None,
                    time + distances[u_elephant][v_elephant] + 1,
                    closed.difference([v_elephant]),
                    rate + nodes[v_elephant],
                    total + rate * (distances[u_elephant][v_elephant] + 1)
                ))
            elif distances[u_elephant][v_elephant] > distances[u_me][v_me]:
                buffer.append((
                    v_me,
                    None,
                    None,
                    None,
                    time + distances[u_me][v_me] + 1,
                    closed.difference([v_me]),
                    rate + nodes[v_me],
                    total + rate * (distances[u_me][v_me] + 1)
                ))
            continue
        
        if len(closed_me) > 0 and len(closed_el) > 0:
            for v_me in sorted(closed_me, key=lambda v: - (26 - (time + distances[u_me][v])) * nodes[v] ):
                for v_elephant in sorted(closed_el, key=lambda v: - (26 - (time + distances[u_elephant][v])) * nodes[v] ):
                    if v_me == v_elephant:
                        continue
                    if time + distances[u_me][v_me] + 1 > 26 and time + distances[u_elephant][v_elephant] + 1 > 26:
                        continue
                    if distances[u_elephant][v_elephant] < distances[u_me][v_me]:
                        buffer.insert(0, (
                            paths[u_me][v_me][distances[u_elephant][v_elephant] + 1],
                            v_me,
                            v_elephant,
                            None,
                            time + distances[u_elephant][v_elephant] + 1,
                            closed.difference([v_elephant]),
                            rate + nodes[v_elephant],
                            total + rate * (distances[u_elephant][v_elephant] + 1)
                        ))
                    elif distances[u_elephant][v_elephant] > distances[u_me][v_me]:
                        buffer.insert(0, (
                            v_me,
                            None,
                            paths[u_elephant][v_elephant][distances[u_me][v_me] + 1],
                            v_elephant,
                            time + distances[u_me][v_me] + 1,
                            closed.difference([v_me]),
                            rate + nodes[v_me],
                            total + rate * (distances[u_me][v_me] + 1)
                        ))
                    else:
                        buffer.insert(0, (
                            v_me,
                            None,
                            v_elephant,
                            None,
                            time + distances[u_me][v_me] + 1,
                            closed.difference([v_me, v_elephant]),
                            rate + nodes[v_me] + nodes[v_elephant],
                            total + rate * (distances[u_me][v_me] + 1)
                        ))
        
        elif len(closed_me) > 0:
            for v_me in sorted(closed_me, key=lambda v: - (26 - (time + distances[u_me][v])) * nodes[v] ):
                if time + distances[u_me][v_me] + 1 > 26:
                    continue
                buffer.insert(0, (
                    v_me,
                    v_me,
                    None,
                    None,
                    time + distances[u_me][v_me] + 1,
                    closed.difference([v_me]),
                    rate + nodes[v_me],
                    total + rate * (distances[u_me][v_me] + 1)
                ))
                
    return max_total


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())