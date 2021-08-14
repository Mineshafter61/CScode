# %% Task 1.1

with open('TIDES.TXT', 'r') as tidesf:
  low_list  = []
  high_list = []
  for tide_data in tidesf:
    date, time, tide, height = tidesf.split('\t')
    height = float(height)
    if tide == "LOW":
      low_list.append((date, time, height))
    else:
      high_list.append((date, time, height))
# find lowest low tide
lowest = min(low[2] for low in low_list)
# find highest high tide
highest = max(high[2] for high in high_list)

print('Height of lowest low tide:', lowest)
print('Height of highest high tide:', highest)


# %% Task 1.2

with open('TIDES.TXT', 'r') as tidesf:
  tide_list = []
  for tide_data in tidesf:
    date, time, tide, height = tidesf.split('\t')
    height = float(height)
    tide_list.append(date, time, tide, height)

tidal_range_list = []
for i in range(len(tide_list)-1):
  # append 2nd date and height
  tidal_range_list.append(( abs(tide_list[i][3] - tide_list[i+1][3]) , tide_list[i+1][0]))

tidal_range_list.sort()
print('Largest tidal range: {0} on {1}'.format(tidal_range_list[-1][0], tidal_range_list[-1][1]))
print('Smallest tidal range: {0} on {1}'.format(tidal_range_list[0][0], tidal_range_list[0][1]))
