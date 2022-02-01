from ctypes.wintypes import OLESTR


def erase_space(equation):
    new_equation = OLESTR.replace(" ", "")
    return new_equation


            