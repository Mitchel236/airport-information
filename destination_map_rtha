import pandas as pd
import branca
import folium

airports = pd.read_csv('airports.csv')

destinations = airports.loc[airports['iata_code'].isin(['RTM', 'AEY', 'AGP', 'AHU', 'ALC', 'LEI',
                                                        'AYT', 'BCN', 'BIA', 'EGC', 'BDS', 'CFU',
                                                        'DBV', 'EDI', 'FAO', 'FEZ', 'FUE', 'GVA',
                                                        'GRO', 'LPA', 'GNB', 'GCI', 'HRG', 'IBZ',
                                                        'INN', 'SAW', 'JER', 'ASR', 'KTT', 'KYA',
                                                        'KGS', 'HER', 'KAO', 'ACE.', 'LIS', 'LCY',
                                                        'RAK', 'BGY', 'MPL', 'NDR', 'OUD', 'PMI',
                                                        'PEG', 'PUY', 'RHO', 'FCO', 'RVN', 'SZG',
                                                        'SSH', 'PMO', 'SFT', 'SPU', 'TNG', 'TFS',
                                                        'TLN', 'VLC', 'ZAD','ZTH'
])]

def popup_html(row):
    i = row
    airport_name=destinations['name'].iloc[i]
    city = destinations['municipality'].iloc[i]
    airport_code = destinations['gps_code'].iloc[i] +" // "+ destinations['iata_code'].iloc[i]        
    airport_elv = destinations['elevation_ft'].iloc[i]
    airport_lat=destinations['latitude_deg'].iloc[i]
    airport_long = destinations['longitude_deg'].iloc[i] 
   

    left_col_color = "#C63038"
    right_col_color = "#f4f4f4"
    
    html = """<!DOCTYPE html>
<html>
<head>

</head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(airport_name) + """

    <table style="height: 126px; width: 350px;">
<tbody>

<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">City</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(city) + """
</tr>

<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Airport Codes</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(airport_code) + """
</tr>

<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Airport Elevation</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(airport_elv) + """
</tr>

<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Latitude</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(airport_lat) + """
</tr>

<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Longitude</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(airport_long) + """
</tr>

</tbody>
</table>
</html>
"""
    return html

location = [51.956902, 4.437220]
m = folium.Map(location=location, zoom_start=3.5, zoom_control=False, scrollwheelzoom=False, dragging=False)

for i in range(0, len(destinations)):
    rtha = destinations['iata_code'].iloc[i]
    if rtha == 'RTM':
        color = '#FFBA08'
    else:
        color='#C63038'

    html = popup_html(i)
    iframe = branca.element.IFrame(html=html,width=510,height=280)
    popup = folium.Popup(folium.Html(html, script=True), max_width=500)

    folium.CircleMarker(
        radius= 2,
        location= [destinations['latitude_deg'].iloc[i], destinations['longitude_deg'].iloc[i]],
        color=color,
        popup= popup
    ).add_to(m)

folium.TileLayer('cartodbdark_matter').add_to(m)
m.save('destination_map.html')