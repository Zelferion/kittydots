#!/usr/bin/env python3
from kitty.cli import parse_args
from kitty.fast_data_types import get_options
import sys

def main(args):
    pass

def handle_result(args, answer, target_window_id, boss):
    step = 1.0
    opts = get_options()
    current_size = opts.font_size
    if args[1] == 'plus':
        amount = step
    elif args[1] == 'minus':
        amount = -step
    elif args[1] == 'reset':
        amount = 0
    else:
        return
    boss.change_font_size(boss.active_window, amount)

handle_result.no_ui = True

if __name__ == '__main__':
    ans = parse_args(['zoom_toggle'] + sys.argv[1:])
    if ans:
        main(ans)
