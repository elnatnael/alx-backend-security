from django.core.management.base import BaseCommand
from ip_tracking.models import BlockedIP
from ipaddress import ip_address, IPv4Address, IPv6Address

class Command(BaseCommand):
    help = 'Add IP addresses to the blacklist'

    def add_arguments(self, parser):
        parser.add_argument('ip_addresses', nargs='+', type=str, help='IP addresses to block')

    def handle(self, *args, **options):
        for ip_str in options['ip_addresses']:
            try:
                # Validate IP address
                ip_obj = ip_address(ip_str)
                ip_to_block = str(ip_obj)
                
                # Create or get existing blocked IP
                _, created = BlockedIP.objects.get_or_create(ip_address=ip_to_block)
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully blocked IP: {ip_to_block}'))
                else:
                    self.stdout.write(self.style.WARNING(f'IP already blocked: {ip_to_block}'))
            except ValueError:
                self.stdout.write(self.style.ERROR(f'Invalid IP address: {ip_str}'))
