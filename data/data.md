# Data Directory Overview

This directory contains data files related to the 2026 Senedd Cymru (Welsh Parliament) constituencies. The files provide geographic boundaries (TopoJSON), hex map layouts (HexJSON), and sample data (CSV).

## Files

### 1. `fake_senedd.csv`
- **Format**: CSV
- **Description**: A simple dataset mapping 2026 Constituency IDs to political parties. This appears to be sample data for testing visualizations, linking a constituency to a winning party.
- **Columns**:
  - `constituency_id`: The identifier for the constituency (e.g., `W000090`).
  - `party`: The name of the political party (e.g., `Labour`, `Plaid Cymru`).

### 2. `senedd_multiple_hexes.csv`
- **Format**: CSV
- **Description**: Detailed data defining a multi-hex layout for the constituencies. In this model, each constituency is represented by multiple hexes (segments), allowing for the visualization of multiple members per constituency.
- **Columns**:
  - `English_Na`: English name of the constituency.
  - `Enw_Cymrae`: Welsh name of the constituency.
  - `No_Rhif`: Constituency number.
  - `Segment`: The segment number (e.g., 1-6) within the constituency.
  - `q`, `r`: Axial coordinates for the hex grid.
  - `name`: Constituency name.
  - `seat_id`: Unique identifier for the specific seat/segment (e.g., `W000091`).
  - `constituency_id`: Identifier for the parent constituency (e.g., `W000090`).
  - `MS`: Name of the Member of the Senedd (likely simulated/placeholder).
  - `Party`: Political party for this specific seat.
  - `id`: A composite ID (e.g., `9_1`).

### 3. `senedd_2026.hexjson`
- **Format**: HexJSON
- **Description**: A standard HexJSON file defining a grid where **one hex represents one constituency**.
- **Usage**: Useful for creating a simplified constituency map where each area has equal visual weight.
- **Key Properties**:
  - Keys are Constituency IDs (e.g., `W000090`).
  - `q`, `r`: Grid coordinates.
  - `English_Na`, `Enw_Cymrae`: Names in English and Welsh.

### 4. `senedd_2026_multiple.hexjson`
- **Format**: HexJSON
- **Description**: A HexJSON file defining a grid where **multiple hexes represent one constituency**. This aligns with the structure in `senedd_multiple_hexes.csv`, typically showing 6 segments per constituency (reflecting the multi-member nature of the new system).
- **Key Properties**:
  - Keys are Seat/Segment IDs (e.g., `W000091`).
  - `constituency_id`: Links back to the parent constituency.
  - `Segment`: Identifies which part of the constituency this hex represents.

### 5. `senedd_2026.topojson`
- **Format**: TopoJSON
- **Description**: Contains the full-resolution vector geographic boundaries for the 16 new Senedd constituencies defined for the 2026 election.
- **Usage**: Best for high-quality geographic maps where precise boundaries are required.

### 6. `senedd_2026_simplified.topojson`
- **Format**: TopoJSON
- **Description**: A simplified version of `senedd_2026.topojson`. The geometry has been simplified to reduce file size and improve rendering performance in web browsers.
- **Usage**: Recommended for web-based interactive maps where loading speed and responsiveness are prioritized over absolute boundary precision.
