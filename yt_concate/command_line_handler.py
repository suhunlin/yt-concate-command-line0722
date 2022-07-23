import sys
import getopt


class CommandLineHandler:
    def run_command_line_opt_parser(self):
        long_opts = 'channel_id= search_word= limit='.split()
        short_opts = 'hc:s:l:'
        key = None
        value = None
        inputs = {}
        try:
            opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
        except getopt.GetoptError:
            self.print_usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                self.print_usage()
                sys.exit(0)
            elif opt in ('-c', '--channel_id'):
                key = 'channel_id'
                value = arg
            elif opt in ('-s', '--search_word'):
                key = 'search_word'
                value = arg
            elif opt in ('-l', '--limit'):
                key = 'limit'
                value = int(arg)
            inputs[key] = value
        return inputs

    def print_usage(self):
        print('python3 yt_concate project OPTIONS')
        print('OPTIONS:')
        print('{:>6} {:<16}{}'.format('-c', '--channel_id', 'Channel id is the Youtube Channel to Download'))
        print('{:>6} {:<16}{}'.format('-s', '--search_word', 'Search the key word from Download Captions'))
        print('{:>6} {:<16}{}'.format('-l', '--limit', 'Video number to edit form Download Video'))
        print('{}'.format('    main.py -c <channel_id> -s <search_word>'))
