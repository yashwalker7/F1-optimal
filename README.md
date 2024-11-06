🏎️***Optimal F1 Track Travel Route Visualization***🏎️

The goal of this project was to find and visualize the optimal travel route between Formula 1 (F1) race locations globally. By calculating an optimized path and visualizing it on a map with an animated plane icon, we aimed to illustrate a potential travel sequence that minimizes travel distance. This approach has practical implications, from cost reduction and time efficiency to significant environmental benefits like lower carbon emissions.

🏎️***Problem Statement***🏎️

In motorsports, teams travel across continents, which contributes to high logistical costs and environmental impacts due to substantial fuel consumption and carbon emissions. The project sought to:

1. Identify the optimal route for visiting F1 tracks worldwide, minimizing total travel distance.
2. Visualize the optimized route on a world map to better illustrate the travel sequence.
3. Animate a plane icon following the route, adding an engaging visual that represents the journey.

🏎️***Solution Approach***🏎️

To address this, we implemented a Python solution that:

1. Calculates the shortest route between F1 race locations using a "nearest neighbor" heuristic.
2. Plots this optimized route on a global map, labeling each track location.
3. Animates a plane icon that moves along the route.
4. Displays the total travel distance and the full travel route as a sequential list.

This solution demonstrates an optimized travel plan that potentially reduces the environmental impact of transporting teams and equipment, a growing concern in sports logistics.

🏎️***Tools & Libraries Used***🏎️

The project was implemented using the following libraries:

**NumPy**: For efficient handling of F1 track coordinates and data manipulation.

**GeoPandas**: To plot the world map, focusing on location-based data in a geographic context.

**Matplotlib**: For plotting and animating the route, and managing geographic labels and the plane icon.

**Geopy**: For calculating precise distances between coordinates based on the Haversine formula.

**Pillow**:  For saving the output animations in GIF format.

 **NOTE:** The geopandas.datasets module has been deprecated. Instead, you can download the world map dataset from Natural Earth and load it into GeoPandas.

 Link: [https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip)



🏎️***Implementation***🏎️

***Data***

The dataset used consists of F1 track coordinates for each location where a race is held. Each entry specifies the latitude and longitude of a specific F1 track. The travel route aims to start from Bahrain and end in Abu Dhabi, covering all other F1 tracks in an optimal sequence.

Steps
***1. Haversine Distance Calculation:***

Using the Haversine formula, we calculated the distance between each pair of F1 tracks, measuring the shortest "great-circle" distance on Earth's surface.

***2. Optimal Route Calculation.(Nearest Neighbor Approach):***

To determine the shortest route, we implemented a nearest neighbor heuristic. Starting at Bahrain, the algorithm repeatedly selects the nearest unvisited track, adding each location to the route until all tracks are visited and the final destination, Abu Dhabi, is reached.
The nearest neighbor approach, while not guaranteeing the absolute shortest route, provides an efficient and reasonable approximation with low computational cost.

***3. Visualization and Animation:***

***GeoPandas World Map***: A shapefile of the world map was loaded and displayed using GeoPandas, allowing us to plot geographic data accurately.

***Optimal Route Plotting***: Using Matplotlib, the optimal route was plotted over the world map with labeled points for each F1 track.

***Moving Plane Icon***: The plane icon was animated along the optimal route, creating an engaging representation of the travel sequence.

***Route Display***: Below the map, the optimal route was listed, showing the specific sequence of tracks.


***4. Environmental and Cost Benefits:***

By visualizing a more efficient travel route, teams could save significant travel time, reduce fuel costs, and minimize CO₂ emissions.

With fewer kilometers traveled, logistics costs decrease, benefiting not only the teams but also the planet by reducing the carbon footprint associated with F1 events.


🏎️***Output***🏎️

The output of the code includes:

***Mapped Route***: A world map displaying the optimized route connecting all F1 tracks.

***Total Distance***: The title displays the total travel distance for the optimized route, useful for understanding potential cost and environmental impacts.

***Plane Animation***: An animated plane icon moves along the route, simulating the actual travel sequence.

***Optimal Route Display***: A sequential list of the optimal route below the map provides a clear understanding of the travel order.

![f1_route_animation](https://github.com/user-attachments/assets/9fffcd01-fb56-4eb4-aab8-16973f089820)
![Screenshot 2024-11-06 142921](https://github.com/user-attachments/assets/3a6b8cbf-030e-45c2-998d-98aa696595c9)


If you calculate the distance between all 24 tracks by air according to the 2024 season's calendar of Formula 1, It takes approx. more than 120,000 km.
But By using Nearest Neighbour Technique as used in this project, The Travel distance is only 68,000 km. Cutting the travel distance by nearly half.

🏎️***1. Environmental Impact:***🏎️

Reducing travel distances can significantly lower CO₂ emissions from flights, which are a major source of greenhouse gases in the logistics sector.
This optimized travel approach promotes sustainability within the sports industry, aligning with the F1’s growing commitment to reducing environmental impact.
This Reduced Emission saves ***Aprrox. 250 trees/person.***

🏎️***2. Cost Savings:***🏎️

Minimizing the travel distance translates to reduced fuel and operational costs for F1 teams and organizers, as transportation is a substantial budget item.
With an efficient route, teams can also minimize wear and tear on equipment, lowering maintenance costs.

If you consider 0.20 USD/km for travelling by Economy for one single person, it costs around 25,000 USD if a person travlled to all 24 races.
Now, If used our Optimal Route, ***It costs 13,000 USD*** considering same conditions as above.

This results in for a Formula 1 team of 100 travelling members saving around ***12,00,000 USD per year.***

🏎️***3. Time Efficiency:***🏎️
A well-planned travel route saves time, which is critical in high-paced environments like F1 where scheduling is paramount.
Reduced travel time allows teams to dedicate more time to training, race preparation, and other critical activities, boosting overall performance.

🏎️***Limitations and Future Enhancements***🏎️

***1. Route Optimization Complexity:***

The nearest neighbor heuristic does not guarantee the absolute shortest route, as it is a greedy approach. Future iterations could implement more sophisticated algorithms (e.g., dynamic programming or simulated annealing) for a closer-to-optimal solution.


***2. Real-World Constraints:***

The model does not currently account for real-world constraints like flight availability, border restrictions, or layover times, which could impact the feasibility of the optimal route.


***3. Interactive Elements:***

Future enhancements could incorporate interactive elements (e.g., clickable labels for more track information or real-time distance updates) to improve user engagement and usability.
