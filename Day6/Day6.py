
def marker_check(buffer_substring):
    buffer_subset = set(buffer_substring)
    if len(buffer_subset) == len(buffer_substring):
        marker=1
    else:
        marker=0
    return marker

def marker_finder(buffer_string, marker_length):
    first_marker = None
    for marker_start, _ in enumerate(buffer_string):
        marker_end = marker_start + marker_length
        if marker_end > len(buffer_string)-1:
            continue
        buffer_substring = buffer_string[marker_start:marker_end]
        if marker_check(buffer_substring) == 1:
            first_marker = marker_end
            break
    return first_marker

with open("input.txt", "r") as f:
    datastream_buffer = f.read()

datastream_packet_marker = marker_finder(datastream_buffer, 4)
print(f"first packet marker after character {datastream_packet_marker}")

datastream_message_marker = marker_finder(datastream_buffer, 14)
print(f"first message marker after character {datastream_message_marker}")