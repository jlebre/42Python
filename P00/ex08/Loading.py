def ft_tqdm(lst: range) -> None:
    """
    Loading bar
    """

    maxim = len(lst)

    for i, obj in enumerate(lst, 1):
        bar = 135
        curr = int((i / maxim) * bar)
        barra = "=" * curr + ">" + " " * (bar - curr)
        if curr == maxim:
            barra = "=" * (curr - 1) + ">" + " " * (bar - curr)
        first = f"{i * 100 // maxim}%|[{barra}]|"
        second = f"{i}/{maxim} [??:??<??:??, ???.??it/s]"
        print(f"\r{first} {second}", end="", flush=True)

        yield obj
    print()

# barra = "█" * curr + " " * (bar - curr)
# print(f"\r{i * 100 // maxim}%|{barra}| {i}/{maxim}\
    # [??:??<??:??, ???.??it/s]", end="", flush=True)
# The commented parts are the new version with "█"
# https://www.youtube.com/watch?v=31Wjc9vZv1s
