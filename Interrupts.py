import sys


class RacecarException(Exception):
    pass


class SigFinish(RacecarException):
    pass


class HazardHalt(RacecarException):
    pass


def throw_signal_function(frame, event, arg):
    raise SigFinish()


def throw_hazard_stop(frame, event, arg):
    raise HazardHalt()


def do_nothing_trace_function(frame, event, arg):
    # Note: each function called will actually call this function
    # so, take care, your program will run slower because of that
    return None


def interrupt_thread(thread):
    for thread_id, frame in sys._current_frames().items():
        if thread_id == thread.ident:
            set_trace_for_frame_and_parents(frame, throw_signal_function)


def set_trace_for_frame_and_parents(frame, trace_func):
    # Note: this only really works if there's a tracing function set in this
    # thread (i.e.: sys.settrace or threading.settrace must have set the
    # function before)
    while frame:
        if frame.f_trace is None:
            frame.f_trace = trace_func
        frame = frame.f_back
    del frame
