#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    print(f'CURRENT LOCATION OF THE ISS:\n Lon:{resp["iss_position"]["longitude"]}\n Lat:{resp["iss_position"]["latitude"]}')

if __name__ == "__main__":
    main()
