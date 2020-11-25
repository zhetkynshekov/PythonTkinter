def _from_rgb(rgba):
    r, g, b, a = rgba
    return f'#{r:02x}{g:02x}{b:02x}{a:02x}'
print(_from_rgb((59, 64, 69, 150)))