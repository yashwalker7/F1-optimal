import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.animation import FuncAnimation, PillowWriter
from math import radians, sin, cos, sqrt, atan2
from geopy.distance import geodesic

# Load world map using Natural Earth dataset
world_map_path = "C:/Users/yashv/Documents/F1 Optimal route/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
world = gpd.read_file(world_map_path)
world = world.to_crs(epsg=4326)  # Convert to WGS84

# F1 Tracks coordinates according to the 2024 calendar of F1 (in WGS84)
f1_tracks = {
    'Bahrain': (26.0309, 50.5158), #would start here
    'Saudi Arabia': (21.6452, 39.1025),
    'Australia': (-37.8487, 144.9574),
    'Japan': (34.8416, 136.5400),
    'China': (31.3399, 121.2210),
    'Miami': (26.0112, -80.2119),
    'Imola': (44.3422, 11.7115),
    'Monaco': (43.7346, 7.4202),
    'Canada': (45.5097, -73.5168),
    'Spain': (41.5697, 2.2571),
    'Austria': (47.2199, 14.7647),
    'England': (52.0736, -1.0218),
    'Hungary': (47.5797, 19.2481),
    'Belgium': (50.4417, 5.9664),
    'Netherlands': (52.3848, 4.5403),
    'Italy': (45.6173, 9.2814),
    'Azerbaijan': (40.3729, 49.8528),
    'Singapore': (1.2913, 103.8635),
    'Austin': (30.1333, -97.6394),
    'Mexico': (19.4052, -99.0926),
    'Brazil': (-23.6999, -46.6965),
    'Las Vegas': (36.1102, -115.1629),
    'Qatar': (25.4901, 51.4516),
    'Abu Dhabi': (24.4696, 54.6047), #would end here
}

track_names = list(f1_tracks.keys())
start = 'Bahrain'
end = 'Abu Dhabi'

# Converting track coordinates to numpy array
track_coords = np.array(list(f1_tracks.values()))

# Haversine distance function
def haversine_distance(coord1, coord2):
    R = 6371.0
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Calculate the optimal route using a nearest neighbor approach
def nearest_neighbor_route():
    unvisited = list(range(1, len(track_coords) - 1))
    route = [0]  # Starting at Bahrain
    total_distance = 0

    current_index = 0
    while unvisited:
        nearest_track = min(unvisited, key=lambda idx: haversine_distance(track_coords[current_index], track_coords[idx]))
        total_distance += haversine_distance(track_coords[current_index], track_coords[nearest_track])
        route.append(nearest_track)
        current_index = nearest_track
        unvisited.remove(nearest_track)

    route.append(len(track_coords) - 1)  # Ending at Abu Dhabi
    total_distance += haversine_distance(track_coords[current_index], track_coords[-1])
    return route, total_distance

# Get optimal route and distance
optimal_route, optimal_distance = nearest_neighbor_route()
optimal_route_coords = track_coords[optimal_route]

#Plot setup
fig, ax = plt.subplots(figsize=(12, 8))
world.plot(ax=ax, color="lightgrey")

# Ploting the optimal path
for i in range(len(optimal_route_coords) - 1):
    start_pt = optimal_route_coords[i]
    end_pt = optimal_route_coords[i + 1]
    plt.plot([start_pt[1], end_pt[1]], [start_pt[0], end_pt[0]], 'bo-', markersize=5, color='blue', linewidth=2)

# Adding Labels
for idx, (lat, lon) in enumerate(optimal_route_coords):
    track_name = track_names[optimal_route[idx]]
    ax.text(lon, lat, track_name, fontsize=8, ha='right', color='darkred')

plt.title(f"Optimal F1 Travel Route - Total Distance: {optimal_distance:.2f} km")

plane_image_path = "C:/Users/yashv/Documents/F1 Optimal route/airplane.png"
plane_img = plt.imread(plane_image_path)

# Annotation box for the plane
image_box = OffsetImage(plane_img, zoom=0.05)
plane_ab = AnnotationBbox(image_box, (optimal_route_coords[0][1], optimal_route_coords[0][0]), frameon=False)
ax.add_artist(plane_ab)

# Animation
def animate(i):
    lat, lon = optimal_route_coords[i]
    plane_ab.xybox = (lon, lat)
    return plane_ab,
ani = FuncAnimation(fig, animate, frames=len(optimal_route_coords), interval=1000, repeat=False)

gif_save_path = "C:/Users/yashv/Downloads/f1_route_animation.gif"
ani.save(gif_save_path, writer=PillowWriter(fps=1))

#Output
optimal_route_text = " -> ".join([track_names[i] for i in optimal_route])
fig.text(0.5, 0.05, f"Optimal Route: {optimal_route_text}", ha='center', fontsize=7, fontweight='bold')

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
