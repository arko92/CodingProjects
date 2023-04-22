# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 00:47:11 2023

@author: arkob

Finite difference methods to calculate the temperature changes over time, given the thermal conductivity, density, and specific heat capacity of the battery pack.

"""

class BatteryCell:
    def __init__(self, capacity, voltage, temperature):
        self.capacity = capacity  # Battery capacity in Ah
        self.voltage = voltage    # Battery voltage in V
        self.temperature = temperature  # Battery temperature in °C

class BatteryPack:
    def __init__(self, n_cells):
        # Create battery cells and add to pack
        self.cells = [BatteryCell(100.0, 3.7, 25.0) for _ in range(n_cells)]

    def set_temperatures(self, temperatures):
        for i in range(len(self.cells)):
            self.cells[i].temperature = temperatures[i]

    def simulate(self, time_step, n_steps):
        # Define constants
        k_thermal = 10.0     # Thermal conductivity (W/mK)
        rho_batt = 1600.0    # Battery pack density (kg/m^3)
        c_p = 800.0          # Specific heat capacity (J/kgK)
        dx = 0.01            # Cell spacing (m)

        # Initialize temperature vector
        temperatures = [25.0] * len(self.cells)

        # Iterate over time and space
        for n in range(n_steps):
            # Compute heat flux for each cell
            heat_flux = [0.0] * len(self.cells)
            for i in range(len(self.cells)):
                # Compute thermal gradient
                T = self.cells[i].temperature
                dTdx = 0.0
                if i > 0:
                    dTdx += (temperatures[i] - temperatures[i-1]) / dx
                if i < len(self.cells) - 1:
                    dTdx += (temperatures[i+1] - temperatures[i]) / dx

                # Compute heat flux
                heat_flux[i] = -k_thermal * rho_batt * c_p * dTdx

            # Compute temperature at next time step
            for i in range(len(self.cells)):
                T = self.cells[i].temperature
                delta_T = heat_flux[i] * time_step / (rho_batt * c_p * dx)
                temperatures[i] = T + delta_T

            # Update cell temperatures
            self.set_temperatures(temperatures)

if __name__ == "__main__":
    battery_pack = BatteryPack(10)

    # Simulate thermal management
    battery_pack.simulate(1.0, 1000)

    # Print final temperatures
    for i, cell in enumerate(battery_pack.cells):
        print(f"Cell {i} temperature: {cell.temperature}")
