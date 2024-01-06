def reachDestination(sx,sy,dx,dy):
    if sx==dx and sy==dy:
        return True
    if sx>dx or sy>dy:
        return False
    if dx>dy:
        return   reachDestination(sx,sy,dx-dy,dy)
    else:
        return reachDestination(sx,sy,dx,dy-dx)

