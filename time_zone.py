#!/usr/bin/python

import GeoIP

#1.4.7
#Europe/Berlin
#Europe/Berlin
#None
#America/Los_Angeles
#America/New_York

print GeoIP.lib_version()
print GeoIP.time_zone_by_country_and_region("DE", 'XY')
print GeoIP.time_zone_by_country_and_region("DE", '')
print GeoIP.time_zone_by_country_and_region("US", "")
print GeoIP.time_zone_by_country_and_region("US", "CA")
print GeoIP.time_zone_by_country_and_region("US", "MA")

