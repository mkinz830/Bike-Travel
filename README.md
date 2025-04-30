# 🚗 Trip Feasibility Checker

This Python script determines whether a vehicle can complete a 1000 km journey based on its fuel capacity, mileage, and the distance between available fuel stations.

---

## 📋 Description

The function `check_trip(fuel_capacity, mileage, fuel_stations)` checks whether a car can make a 1000 km trip given:
- `fuel_capacity` (in liters)
- `mileage` (km per liter)
- `fuel_stations` (maximum distance between fuel stations in km)

---

## 🧮 How It Works

1. **Calculate maximum distance per full tank**  
   `total_distance_per_tank = fuel_capacity × mileage`

2. **Decision Logic**:
   - If the vehicle can travel **1000 km or more on a full tank**, return `'Yes 1'`
   - If the vehicle **can't reach 1000 km in one tank** but can **travel far enough to reach the next fuel station**, return `'Yes X'`, where `X` is the number of required stops (`1000 // distance_per_tank + 1`)
   - If the distance per tank is **less than the distance between fuel stations**, return `'No'`
