mapboxgl.accessToken = 'pk.eyJ1IjoibWFyaWlhbW0iLCJhIjoiY2xwYmE2bWVoMGhwczJrcXIxNzlvaTgyaiJ9.rDjlQgOMAzkppYwBVeUG2Q';

// Map initialization 
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11', // Choose the map style
    center: [31.2357, 30.0444], // Center of Cairo, Egypt
    zoom: 16 // Zoom level adjusted for visibility
});

// Car icon
var carIcon = document.createElement('div');
carIcon.className = 'car-icon';
carIcon.style.backgroundImage = 'url("./black_car.JPG")';
carIcon.style.width = '30px';
carIcon.style.height = '30px';
carIcon.style.backgroundSize = 'cover';

// Initialize marker with car icon
var marker = new mapboxgl.Marker(carIcon)
    .setLngLat([31.2357, 30.0444]) // Initial position set to Cairo
    .addTo(map);

if (!navigator.geolocation) {
    console.log("Your browser doesn't support geolocation feature!");
} else {
    setInterval(() => {
        simulateMovingCar();
    }, 500);
}

function simulateMovingCar() {
    // Update marker's position to simulate car movement
    var newLng = marker.getLngLat().lng + 0.0001; // Adjust the movement increment as needed
    var newLat = marker.getLngLat().lat; // Adjust the movement increment as needed    //edited it 

    marker.setLngLat([newLng, newLat]);

    /*var bounds = new mapboxgl.LngLatBounds(
        [newLng - 0.01, newLat - 0.01],
        [newLng + 0.01, newLat + 0.01]
    );

    map.fitBounds(bounds);*/

    map.panTo([newLng, newLat]);

    //console.log("Car is moving to: Lat: " + newLat + " Long: " + newLng);
}
