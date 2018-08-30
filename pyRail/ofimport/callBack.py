#================IO flush====================
termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
__stdin__.flush()
__stdout__.flush()
get.stop = True
exit()