#!/usr/bin/env python3
import json
import sys

DROPPED_EVENTS = {"scroll", "video_progress", "form_start", "user_engagement"}

def filter_event_batch(incoming_json):
    events = json.loads(incoming_json) if isinstance(incoming_json, str) else incoming_json
    retained = [e for e in events if e.get("event_name") not in DROPPED_EVENTS]
    dropped = len(events) - len(retained)
    return retained, dropped

if __name__ == "__main__":
    test_events = [{"event_name": "scroll"}, {"event_name": "purchase"}, {"event_name": "video_progress"}]
    ret, drop = filter_event_batch(test_events)
    print(f"Filtered {drop} noise events. Retained {len(ret)} high-value commercial events.")
