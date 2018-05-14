import bashcolor
from pyannotate_runtime import collect_types

if __name__ == '__main__':
    collect_types.init_types_collection()
    with collect_types.collect():

        bashcolor.print_colors()

        bashcolor.colorize("test", bashcolor.BLACK, bashcolor.RED, [bashcolor.BOLD])
        bashcolor.colorize("test", color_256=16, background_256=164)

    collect_types.dump_stats('type_info.json')
