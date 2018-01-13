# read_last_n_lines

I needed a python lib/method which can read a file from the end and return last couple of lines.
So I wrote this library which has a method which returns last n lines when invoked.
It is not a memory intensive function since it doesn't read the whole file at once and store in memory.
It reads one line at a time.
