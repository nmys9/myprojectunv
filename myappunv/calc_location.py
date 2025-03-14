import numpy as np

def calculate_location(received_data,fingerprint_list):
    location_scores={}
    
    for received_ap in received_data:
        for stored_fp in fingerprint_list:
            if received_ap['bssid']==stored_fp['bssid']:
                rssi_diff=abs(received_ap['rssi']-(stored_fp['rssi_min']+stored_fp['rssi_max'])/2)
                weight=1/(rssi_diff+1)
                location_scores[stored_fp['location_name']]=location_scores.get(stored_fp['location_name'],0)+weight