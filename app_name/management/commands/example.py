from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/
    help = "Example command to copy and build from"

    def add_arguments(self, parser):
        # https://docs.python.org/3/library/argparse.html

        parser.add_argument(
            'positional_arg',
            help="Positional value example")

        parser.add_argument(
            "--optional_value",
            action="store_const",
            type=int,  # str also allowed, see argparse docs
            help="Optional input value example")

        parser.add_argument(
            "--optional_boolean",
            action="store_true",
            help="Optional input value example")

    def handle(self, *args, **options):
        positional_arg = options['positional_arg']
        optional_value = options['optional_value']
        optional_boolean = options['optional_boolean']

        print(f"Positional Arg: {positional_arg}")
        print(f"Optional Value: {optional_value or 'not set'}")
        print(f"Optional Boolean: {optional_boolean}")
