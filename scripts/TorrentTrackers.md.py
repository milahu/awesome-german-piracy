#!/usr/bin/env python3

# generate Pages/TorrentTrackers.md

import os
import sys
import csv

# based on https://github.com/HDVinnie/Private-Trackers-Spreadsheet/issues/177
input_csv = os.path.dirname(sys.argv[0]) + "/TorrentTrackers.md.csv"

with open(input_csv, newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)

    print("# Torrent Trackers")
    print()
    head_columns = [
        "Website",
        "Status",
        "Remark",
        "Main language",
    ]
    print("|" + "|".join(head_columns) + "|")
    print("|-" * len(head_columns) + "|")
    for row in reader:
        website_name = row["Name"]
        website_url = row["Website"]
        shield_image_url = "https://img.shields.io/website?down_color=red&down_message=offline&up_color=green&up_message=online&url=" + website_url
        remark = row["Join"]
        body_columns = [
            f"[{website_name}]({website_url})",
            f"[![{website_name}]({shield_image_url})]({website_url})",
            remark,
            "🇩🇪",
        ]
        print("|" + "|".join(body_columns) + "|")
