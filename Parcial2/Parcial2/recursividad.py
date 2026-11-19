def limpiar_feed(publicaciones):
    if len(publicaciones) <= 1:
        return publicaciones

    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    else:
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

publicaciones = ["Post A", "Post B", "Post B", "Post C", "Post B"]
print(limpiar_feed(publicaciones))