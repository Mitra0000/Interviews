# Simple graph that roughly represents the London tube map.
# While most distances come from real data, the gaps were filled in with estimations
# so this graph isn't fully accurate.
tube_map = {
  "Harrow & Wealdstone": {
    "Kenton": 2.23
  },
  "Kenton": {
    "Harrow & Wealdstone": 2.38,
    "South Kenton": 1.88
  },
  "South Kenton": {
    "Kenton": 2.0,
    "North Wembley": 1.5
  },
  "North Wembley": {
    "South Kenton": 1.58,
    "Wembley Central": 1.92
  },
  "Wembley Central": {
    "North Wembley": 1.95,
    "Stonebridge Park": 2.23
  },
  "Stonebridge Park": {
    "Wembley Central": 2.42,
    "Harlesden": 2.13
  },
  "Harlesden": {
    "Stonebridge Park": 2.02,
    "Willesden Junction": 1.65
  },
  "Willesden Junction": {
    "Harlesden": 1.63,
    "Kensal Green": 2.47
  },
  "Kensal Green": {
    "Willesden Junction": 2.53,
    "Queen's Park": 2.65
  },
  "Queen's Park": {
    "Kensal Green": 2.83,
    "Kilburn Park": 1.42
  },
  "Kilburn Park": {
    "Queen's Park": 2.1,
    "Maida Vale": 1.48
  },
  "Maida Vale": {
    "Kilburn Park": 1.48,
    "Warwick Avenue": 1.5
  },
  "Warwick Avenue": {
    "Maida Vale": 1.5,
    "Paddington": 1.58
  },
  "Paddington": {
    "Warwick Avenue": 1.63,
    "Edgware Road": 2.15,
    "Royal Oak": 1.33,
    "Bayswater": 1.65,
    "Bond Street": 1,
    "Acton Main Line": 1
  },
  "Edgware Road": {
    "Paddington": 1.85,
    "Marylebone": 1.12,
    "Baker Street": 1.47,
    "Royal Oak": 1
  },
  "Marylebone": {
    "Edgware Road": 1.08,
    "Baker Street": 1.17
  },
  "Baker Street": {
    "Marylebone": 1.08,
    "Regent's Park": 1.68,
    "Edgware Road": 1.88,
    "Great Portland Street": 1.9,
    "St. John's Wood": 2.85,
    "Bond Street": 2.1,
    "Finchley Road": 5.55
  },
  "Regent's Park": {
    "Baker Street": 1.65,
    "Oxford Circus": 1.85
  },
  "Oxford Circus": {
    "Regent's Park": 1.72,
    "Piccadilly Circus": 1.95,
    "Bond Street": 1.03,
    "Tottenham Court Road": 0.98,
    "Green Park": 1.78,
    "Warren Street": 1.53
  },
  "Piccadilly Circus": {
    "Oxford Circus": 2.02,
    "Charing Cross": 1.35,
    "Green Park": 1.18,
    "Leicester Square": 1.17
  },
  "Charing Cross": {
    "Piccadilly Circus": 1.6,
    "Embankment": 0.8,
    "Leicester Square": 1.17
  },
  "Embankment": {
    "Charing Cross": 0.87,
    "Waterloo": 1.37,
    "Temple": 1.37,
    "Westminster": 1.4
  },
  "Waterloo": {
    "Embankment": 1.4,
    "Lambeth North": 1.45,
    "Westminster": 1.43,
    "Southwark": 1.02,
    "Kennington": 2.97
  },
  "Lambeth North": {
    "Waterloo": 1.45,
    "Elephant & Castle": 2.57
  },
  "Elephant & Castle": {
    "Lambeth North": 2.13,
    "Kennington": 2.03,
    "Borough": 1.75
  },
  "West Ruislip": {
    "Ruislip Gardens": 2.28
  },
  "Ruislip Gardens": {
    "West Ruislip": 2.68,
    "South Ruislip": 1.3
  },
  "South Ruislip": {
    "Ruislip Gardens": 1.37,
    "Northolt": 2.23
  },
  "Northolt": {
    "South Ruislip": 2.25,
    "Greenford": 1.93
  },
  "Greenford": {
    "Northolt": 2.15,
    "Perivale": 1.85
  },
  "Perivale": {
    "Greenford": 2.0,
    "Hanger Lane": 2.1
  },
  "Hanger Lane": {
    "Perivale": 2.07,
    "North Acton": 2.85
  },
  "North Acton": {
    "Hanger Lane": 2.87,
    "East Acton": 1.5,
    "West Acton": 2.52
  },
  "East Acton": {
    "North Acton": 1.57,
    "White City": 2.57
  },
  "White City": {
    "East Acton": 2.67,
    "Shepherd's Bush": 2.68
  },
  "Shepherd's Bush": {
    "White City": 2.77,
    "Holland Park": 1.37
  },
  "Holland Park": {
    "Shepherd's Bush": 1.52,
    "Notting Hill Gate": 1.08
  },
  "Notting Hill Gate": {
    "Holland Park": 1.18,
    "Queensway": 1.17,
    "High Street Kensington": 1.58,
    "Bayswater": 1.77
  },
  "Queensway": {
    "Notting Hill Gate": 1.18,
    "Lancaster Gate": 1.35
  },
  "Lancaster Gate": {
    "Queensway": 1.65,
    "Marble Arch": 1.92
  },
  "Marble Arch": {
    "Lancaster Gate": 1.62,
    "Bond Street": 1.0
  },
  "Bond Street": {
    "Marble Arch": 1.02,
    "Oxford Circus": 1.1,
    "Baker Street": 2.28,
    "Green Park": 1.78,
    "Tottenham Court Road": 1,
    "Paddington": 1
  },
  "Tottenham Court Road": {
    "Oxford Circus": 1.02,
    "Holborn": 1.63,
    "Leicester Square": 0.98,
    "Goodge Street": 1.28,
    "Farringdon": 1,
    "Bond Street": 1
  },
  "Holborn": {
    "Tottenham Court Road": 1.38,
    "Chancery Lane": 0.87,
    "Covent Garden": 1.53,
    "Russell Square": 1.55
  },
  "Chancery Lane": {
    "Holborn": 0.85,
    "St. Paul's": 1.52
  },
  "St. Paul's": {
    "Chancery Lane": 1.52,
    "Bank": 1.62
  },
  "Bank": {
    "St. Paul's": 1.63,
    "Liverpool Street": 1.62,
    "London Bridge": 1.55,
    "Moorgate": 1.77,
    "Waterloo  ": 1,
    "Shadwell": 1
  },
  "Liverpool Street": {
    "Bank": 1.65,
    "Bethnal Green": 2.6,
    "Moorgate": 1.32,
    "Aldgate": 2.18,
    "Aldgate East": 1.93,
    "Whitechapel": 1,
    "Farringdon": 1
  },
  "Bethnal Green": {
    "Liverpool Street": 2.77,
    "Mile End": 1.98
  },
  "Mile End": {
    "Bethnal Green": 1.97,
    "Stratford": 3.18,
    "Stepney Green": 1.72,
    "Bow Road": 1.27
  },
  "Stratford": {
    "Mile End": 3.03,
    "Leyton": 2.4,
    "West Ham": 2.42,
    "Pudding Mill Lane": 1,
    "Stratford International": 1,
    "Stratford High Street": 1,
    "Maryland": 1,
    "Whitechapel": 1
  },
  "Leyton": {
    "Stratford": 2.43,
    "Leytonstone": 2.02
  },
  "Leytonstone": {
    "Leyton": 2.02,
    "Snaresbrook": 1.8,
    "Wanstead": 2.15
  },
  "Snaresbrook": {
    "Leytonstone": 2.05,
    "South Woodford": 1.62
  },
  "South Woodford": {
    "Snaresbrook": 1.6,
    "Woodford": 1.9
  },
  "Woodford": {
    "South Woodford": 1.95,
    "Buckhurst Hill": 2.28,
    "Roding Valley": 2.18
  },
  "Buckhurst Hill": {
    "Woodford": 2.32,
    "Loughton": 2.35
  },
  "Loughton": {
    "Buckhurst Hill": 2.07,
    "Debden": 2.13
  },
  "Debden": {
    "Loughton": 2.67,
    "Theydon Bois": 3.0
  },
  "Theydon Bois": {
    "Debden": 2.88,
    "Epping": 2.6
  },
  "Epping": {
    "Theydon Bois": 2.37
  },
  "Ealing Broadway": {
    "West Acton": 2.28,
    "Ealing Common": 2.67,
    "Acton Main Line": 1,
    "West Ealing": 1
  },
  "West Acton": {
    "Ealing Broadway": 3.07,
    "North Acton": 2.3
  },
  "Wanstead": {
    "Leytonstone": 2.17,
    "Redbridge": 1.62
  },
  "Redbridge": {
    "Wanstead": 1.58,
    "Gants Hill": 1.65
  },
  "Gants Hill": {
    "Redbridge": 1.7,
    "Newbury Park": 2.68
  },
  "Newbury Park": {
    "Gants Hill": 2.73,
    "Barkingside": 1.55
  },
  "Barkingside": {
    "Newbury Park": 1.58,
    "Fairlop": 1.57
  },
  "Fairlop": {
    "Barkingside": 1.57,
    "Hainault": 2.93
  },
  "Hainault": {
    "Fairlop": 1.82,
    "Grange Hill": 1.73
  },
  "Roding Valley": {
    "Woodford": 2.03,
    "Chigwell": 2.13
  },
  "Chigwell": {
    "Roding Valley": 2.45,
    "Grange Hill": 1.73
  },
  "Grange Hill": {
    "Chigwell": 1.63,
    "Hainault": 1.7
  },
  "Hammersmith": {
    "Goldhawk Road": 2.05,
    "Ravenscourt Park": 1.63,
    "Barons Court": 1.43
  },
  "Goldhawk Road": {
    "Hammersmith": 2.43,
    "Shepherd's Bush Market": 1.15
  },
  "Shepherd's Bush Market": {
    "Goldhawk Road": 1.15,
    "Wood Lane": 0.7
  },
  "Wood Lane": {
    "Shepherd's Bush Market": 0.7,
    "Latimer Road": 0.93
  },
  "Latimer Road": {
    "Wood Lane": 0.93,
    "Ladbroke Grove": 1.37
  },
  "Ladbroke Grove": {
    "Latimer Road": 1.28,
    "Westbourne Park": 1.48
  },
  "Westbourne Park": {
    "Ladbroke Grove": 1.48,
    "Royal Oak": 1.78
  },
  "Royal Oak": {
    "Westbourne Park": 1.72,
    "Paddington": 1.52,
    "Edgware Road": 1
  },
  "Great Portland Street": {
    "Baker Street": 1.57,
    "Euston Square": 1.25
  },
  "Euston Square": {
    "Great Portland Street": 1.3,
    "King's Cross St. Pancras": 1.75
  },
  "King's Cross St. Pancras": {
    "Euston Square": 1.65,
    "Farringdon": 2.98,
    "Angel": 1,
    "Euston": 1,
    "Russell Square": 1,
    "Caledonian Road": 1,
    "Highbury & Islington": 1
  },
  "Farringdon": {
    "King's Cross St. Pancras": 3.12,
    "Barbican": 1.22,
    "Liverpool Street": 1,
    "Tottenham Court Road": 1
  },
  "Barbican": {
    "Farringdon": 1.2,
    "Moorgate": 1.32
  },
  "Moorgate": {
    "Barbican": 1.38,
    "Liverpool Street": 1.18,
    "Bank": 1.9,
    "Old Street": 1.45
  },
  "Aldgate": {
    "Liverpool Street": 1.75,
    "Tower Hill": 1.37
  },
  "Tower Hill": {
    "Aldgate": 1.3,
    "Monument": 1.48,
    "Aldgate East": 1.88
  },
  "Monument": {
    "Tower Hill": 1.8,
    "Cannon Street": 0.88
  },
  "Cannon Street": {
    "Monument": 0.97,
    "Mansion House": 0.93
  },
  "Mansion House": {
    "Cannon Street": 0.98,
    "Blackfriars": 1.22
  },
  "Blackfriars": {
    "Mansion House": 1.52,
    "Temple": 1.37
  },
  "Temple": {
    "Blackfriars": 1.4,
    "Embankment": 1.43
  },
  "Westminster": {
    "Embankment": 1.37,
    "St. James's Park": 1.52,
    "Green Park": 1.82,
    "Waterloo": 1.38
  },
  "St. James's Park": {
    "Westminster": 1.5,
    "Victoria": 1.33
  },
  "Victoria": {
    "St. James's Park": 1.42,
    "Sloane Square": 1.75,
    "Pimlico": 1.83,
    "Green Park": 1.95
  },
  "Sloane Square": {
    "Victoria": 1.8,
    "South Kensington": 2.0
  },
  "South Kensington": {
    "Sloane Square": 1.98,
    "Gloucester Road": 1.48,
    "Knightsbridge": 2.48
  },
  "Gloucester Road": {
    "South Kensington": 1.43,
    "High Street Kensington": 2.23,
    "Earl's Court": 1.82
  },
  "High Street Kensington": {
    "Gloucester Road": 1.8,
    "Notting Hill Gate": 1.68,
    "Earl's Court": 2.72
  },
  "Bayswater": {
    "Notting Hill Gate": 1.47,
    "Paddington": 1.63
  },
  "Ealing Common": {
    "Ealing Broadway": 3.5,
    "Acton Town": 1.9,
    "North Ealing": 1.88
  },
  "Acton Town": {
    "Ealing Common": 1.5,
    "Chiswick Park": 1.8,
    "Turnham Green": 1,
    "South Ealing": 2.8
  },
  "Chiswick Park": {
    "Acton Town": 1.83,
    "Turnham Green": 1.48
  },
  "Turnham Green": {
    "Chiswick Park": 1.58,
    "Stamford Brook": 1.15,
    "Gunnersbury": 2.28,
    "Acton Town": 1,
    "Hammersmith (Dist&Picc Line)": 1
  },
  "Stamford Brook": {
    "Turnham Green": 1.17,
    "Ravenscourt Park": 1.4
  },
  "Ravenscourt Park": {
    "Stamford Brook": 1.37,
    "Hammersmith": 1.85
  },
  "Barons Court": {
    "Hammersmith": 1.33,
    "West Kensington": 1.28,
    "Hammersmith (Dist&Picc Line)": 1,
    "Earl's Court": 2.55
  },
  "West Kensington": {
    "Barons Court": 1.32,
    "Earl's Court": 2.17
  },
  "Earl's Court": {
    "West Kensington": 1.62,
    "Gloucester Road": 1.92,
    "High Street Kensington": 3.05,
    "West Brompton": 1.42,
    "Kensington (Olympia)": 1,
    "Barons Court": 2.68
  },
  "Aldgate East": {
    "Tower Hill": 1.87,
    "Whitechapel": 2.17,
    "Liverpool Street": 2.12
  },
  "Whitechapel": {
    "Aldgate East": 2.18,
    "Stepney Green": 2.05,
    "Canary Wharf": 1,
    "Liverpool Street": 1,
    "Stratford": 1
  },
  "Stepney Green": {
    "Whitechapel": 2.63,
    "Mile End": 1.73
  },
  "Bow Road": {
    "Mile End": 1.27,
    "Bromley-by-Bow": 2.12
  },
  "Bromley-by-Bow": {
    "Bow Road": 2.23,
    "West Ham": 2.0
  },
  "West Ham": {
    "Bromley-by-Bow": 2.12,
    "Plaistow": 1.43,
    "Canning Town": 2.13,
    "Stratford": 3.15,
    "Abbey Road": 1,
    "Star Lane": 1
  },
  "Plaistow": {
    "West Ham": 1.5,
    "Upton Park": 1.97
  },
  "Upton Park": {
    "Plaistow": 1.93,
    "East Ham": 2.02
  },
  "East Ham": {
    "Upton Park": 2.0,
    "Barking": 3.78
  },
  "Barking": {
    "East Ham": 2.87,
    "Upney": 1.97
  },
  "Upney": {
    "Barking": 1.92,
    "Becontree": 2.33
  },
  "Becontree": {
    "Upney": 2.33,
    "Dagenham Heathway": 1.88
  },
  "Dagenham Heathway": {
    "Becontree": 1.88,
    "Dagenham East": 1.85
  },
  "Dagenham East": {
    "Dagenham Heathway": 1.83,
    "Elm Park": 2.85
  },
  "Elm Park": {
    "Dagenham East": 2.77,
    "Hornchurch": 2.05
  },
  "Hornchurch": {
    "Elm Park": 1.98,
    "Upminster Bridge": 1.77
  },
  "Upminster Bridge": {
    "Hornchurch": 1.78,
    "Upminster": 2.32
  },
  "Upminster": {
    "Upminster Bridge": 2.08
  },
  "Richmond": {
    "Kew Gardens": 3.1
  },
  "Kew Gardens": {
    "Richmond": 4.1,
    "Gunnersbury": 2.42
  },
  "Gunnersbury": {
    "Kew Gardens": 2.43,
    "Turnham Green": 2.6
  },
  "Wimbledon": {
    "Wimbledon Park": 2.82
  },
  "Wimbledon Park": {
    "Wimbledon": 3.5,
    "Southfields": 2.18
  },
  "Southfields": {
    "Wimbledon Park": 2.05,
    "East Putney": 2.37
  },
  "East Putney": {
    "Southfields": 2.35,
    "Putney Bridge": 1.85
  },
  "Putney Bridge": {
    "East Putney": 2.18,
    "Parsons Green": 1.92
  },
  "Parsons Green": {
    "Putney Bridge": 2.32,
    "Fulham Broadway": 1.48
  },
  "Fulham Broadway": {
    "Parsons Green": 1.5,
    "West Brompton": 1.57
  },
  "West Brompton": {
    "Fulham Broadway": 1.55,
    "Earl's Court": 1.42
  },
  "Kensington (Olympia)": {
    "Earl's Court": 1
  },
  "Stanmore": {
    "Canons Park": 1.95
  },
  "Canons Park": {
    "Stanmore": 2.87,
    "Queensbury": 1.93
  },
  "Queensbury": {
    "Canons Park": 2.23,
    "Kingsbury": 1.72
  },
  "Kingsbury": {
    "Queensbury": 1.85,
    "Wembley Park": 3.47
  },
  "Wembley Park": {
    "Kingsbury": 3.47,
    "Neasden": 2.6,
    "Preston Road": 2.12,
    "Finchley Road": 7.0
  },
  "Neasden": {
    "Wembley Park": 2.65,
    "Dollis Hill": 1.43
  },
  "Dollis Hill": {
    "Neasden": 1.38,
    "Willesden Green": 1.8
  },
  "Willesden Green": {
    "Dollis Hill": 1.67,
    "Kilburn": 1.68
  },
  "Kilburn": {
    "Willesden Green": 2.07,
    "West Hampstead": 1.63
  },
  "West Hampstead": {
    "Kilburn": 1.55,
    "Finchley Road": 1.25
  },
  "Finchley Road": {
    "West Hampstead": 1.2,
    "Swiss Cottage": 1.18,
    "Wembley Park": 7.05,
    "Baker Street": 6.13
  },
  "Swiss Cottage": {
    "Finchley Road": 1.18,
    "St. John's Wood": 1.52
  },
  "St. John's Wood": {
    "Swiss Cottage": 1.52,
    "Baker Street": 2.77
  },
  "Green Park": {
    "Bond Street": 1.82,
    "Westminster": 1.87,
    "Hyde Park Corner": 1.73,
    "Piccadilly Circus": 1.1,
    "Victoria": 1.88,
    "Oxford Circus": 1.97
  },
  "Southwark": {
    "Waterloo": 0.97,
    "London Bridge": 1.65
  },
  "London Bridge": {
    "Southwark": 1.77,
    "Bermondsey": 2.25,
    "Borough": 1.45,
    "Bank": 1.53
  },
  "Bermondsey": {
    "London Bridge": 2.17,
    "Canada Water": 1.48
  },
  "Canada Water": {
    "Bermondsey": 1.52,
    "Canary Wharf": 2.5
  },
  "Canary Wharf": {
    "Canada Water": 2.63,
    "North Greenwich": 2.23,
    "Westferry": 1,
    "Heron Quays": 1,
    "West India Quay": 1,
    "Custom House": 1,
    "Whitechapel": 1
  },
  "North Greenwich": {
    "Canary Wharf": 1.98,
    "Canning Town": 2.15
  },
  "Canning Town": {
    "North Greenwich": 2.17,
    "West Ham": 2.15,
    "East India": 1,
    "West Silvertown": 1,
    "Star Lane": 1,
    "Royal Victoria": 1
  },
  "Chesham": {
    "Chalfont & Latimer": 9.63
  },
  "Chalfont & Latimer": {
    "Chesham": 9.48,
    "Chorleywood": 3.68,
    "Amersham": 4.07
  },
  "Chorleywood": {
    "Chalfont & Latimer": 3.95,
    "Rickmansworth": 4.07
  },
  "Rickmansworth": {
    "Chorleywood": 4.03,
    "Moor Park": 3.78
  },
  "Moor Park": {
    "Rickmansworth": 4.13,
    "Northwood": 2.87,
    "Croxley": 4.33
  },
  "Northwood": {
    "Moor Park": 2.55,
    "Northwood Hills": 2.2
  },
  "Northwood Hills": {
    "Northwood": 2.23,
    "Pinner": 2.48
  },
  "Pinner": {
    "Northwood Hills": 2.6,
    "North Harrow": 2.08
  },
  "North Harrow": {
    "Pinner": 2.0,
    "Harrow-on-the-Hill": 1
  },
  "Harrow-on-the-Hill": {
    "North Harrow": 1,
    "Northwick Park": 1,
    "West Harrow": 1
  },
  "Northwick Park": {
    "Harrow-on-the-Hill": 1,
    "Preston Road": 2.05
  },
  "Preston Road": {
    "Northwick Park": 2.3,
    "Wembley Park": 1.98
  },
  "Amersham": {
    "Chalfont & Latimer": 3.65
  },
  "Uxbridge": {
    "Hillingdon": 3.0
  },
  "Hillingdon": {
    "Uxbridge": 4.08,
    "Ickenham": 1.73
  },
  "Ickenham": {
    "Hillingdon": 1.75,
    "Ruislip": 2.45
  },
  "Ruislip": {
    "Ickenham": 2.57,
    "Ruislip Manor": 1.45
  },
  "Ruislip Manor": {
    "Ruislip": 1.35,
    "Eastcote": 1.82
  },
  "Eastcote": {
    "Ruislip Manor": 1.82,
    "Rayners Lane": 2.33
  },
  "Rayners Lane": {
    "Eastcote": 2.23,
    "West Harrow": 2.08,
    "South Harrow": 2.58
  },
  "West Harrow": {
    "Rayners Lane": 2.05,
    "Harrow-on-the-Hill": 1
  },
  "Watford": {
    "Croxley": 3.22
  },
  "Croxley": {
    "Watford": 3.6,
    "Moor Park": 4.42
  },
  "Morden": {
    "South Wimbledon": 2.35
  },
  "South Wimbledon": {
    "Morden": 2.95,
    "Colliers Wood": 1.85
  },
  "Colliers Wood": {
    "South Wimbledon": 1.88,
    "Tooting Broadway": 1.97
  },
  "Tooting Broadway": {
    "Colliers Wood": 1.98,
    "Tooting Bec": 1.88
  },
  "Tooting Bec": {
    "Tooting Broadway": 1.77,
    "Balham": 1.65
  },
  "Balham": {
    "Tooting Bec": 1.67,
    "Clapham South": 1.8
  },
  "Clapham South": {
    "Balham": 1.88,
    "Clapham Common": 2.2
  },
  "Clapham Common": {
    "Clapham South": 2.0,
    "Clapham North": 1.32
  },
  "Clapham North": {
    "Clapham Common": 1.4,
    "Stockwell": 1.72
  },
  "Stockwell": {
    "Clapham North": 1.55,
    "Oval": 2.03,
    "Brixton": 2.03,
    "Vauxhall": 2.23
  },
  "Oval": {
    "Stockwell": 2.2,
    "Kennington": 1.7
  },
  "Kennington": {
    "Oval": 1.58,
    "Waterloo": 2.77,
    "Nine Elms": 1,
    "Elephant & Castle": 1.8
  },
  "Leicester Square": {
    "Charing Cross": 1.2,
    "Tottenham Court Road": 1.03,
    "Piccadilly Circus": 1.07,
    "Covent Garden": 0.77
  },
  "Goodge Street": {
    "Tottenham Court Road": 1.32,
    "Warren Street": 1.07
  },
  "Warren Street": {
    "Goodge Street": 1.07,
    "Euston": 1.18,
    "Oxford Circus": 1.72
  },
  "Euston": {
    "Warren Street": 1.18,
    "Mornington Crescent": 1.53,
    "King's Cross St. Pancras": 1,
    "Camden Town": 3.88
  },
  "Mornington Crescent": {
    "Euston": 1.52,
    "Camden Town": 1.8
  },
  "Camden Town": {
    "Mornington Crescent": 1.63,
    "Chalk Farm": 1.55,
    "Kentish Town": 1.95,
    "Euston": 2.95
  },
  "Chalk Farm": {
    "Camden Town": 1.53,
    "Belsize Park": 1.9
  },
  "Belsize Park": {
    "Chalk Farm": 1.77,
    "Hampstead": 2.02
  },
  "Hampstead": {
    "Belsize Park": 1.82,
    "Golders Green": 3.95
  },
  "Golders Green": {
    "Hampstead": 3.42,
    "Brent Cross": 2.22
  },
  "Brent Cross": {
    "Golders Green": 2.57,
    "Hendon Central": 1.83
  },
  "Hendon Central": {
    "Brent Cross": 1.73,
    "Colindale": 2.67
  },
  "Colindale": {
    "Hendon Central": 2.83,
    "Burnt Oak": 2.07
  },
  "Burnt Oak": {
    "Colindale": 1.98,
    "Edgware": 3.37
  },
  "Edgware": {
    "Burnt Oak": 2.43
  },
  "Battersea Power Station": {
    "Nine Elms": 1
  },
  "Nine Elms": {
    "Battersea Power Station": 1,
    "Kennington": 1
  },
  "Kentish Town": {
    "Camden Town": 1.93,
    "Tufnell Park": 1.58
  },
  "Tufnell Park": {
    "Kentish Town": 1.42,
    "Archway": 1.68
  },
  "Archway": {
    "Tufnell Park": 1.6,
    "Highgate": 2.75
  },
  "Highgate": {
    "Archway": 2.8,
    "East Finchley": 2.62
  },
  "East Finchley": {
    "Highgate": 3.0,
    "Finchley Central": 3.1
  },
  "Finchley Central": {
    "East Finchley": 3.37,
    "West Finchley": 2.1,
    "Mill Hill East": 2.98
  },
  "West Finchley": {
    "Finchley Central": 2.08,
    "Woodside Park": 1.55
  },
  "Woodside Park": {
    "West Finchley": 1.7,
    "Totteridge & Whetstone": 2.23
  },
  "Totteridge & Whetstone": {
    "Woodside Park": 2.23,
    "High Barnet": 4.62
  },
  "High Barnet": {
    "Totteridge & Whetstone": 3.67
  },
  "Borough": {
    "Elephant & Castle": 1.72,
    "London Bridge": 1.4
  },
  "Old Street": {
    "Moorgate": 1.37,
    "Angel": 2.43
  },
  "Angel": {
    "Old Street": 2.87,
    "King's Cross St. Pancras": 1
  },
  "Mill Hill East": {
    "Finchley Central": 2.75
  },
  "South Harrow": {
    "Rayners Lane": 2.4,
    "Sudbury Hill": 1.85
  },
  "Sudbury Hill": {
    "South Harrow": 2.05,
    "Sudbury Town": 2.03
  },
  "Sudbury Town": {
    "Sudbury Hill": 2.25,
    "Alperton": 1.95
  },
  "Alperton": {
    "Sudbury Town": 2.03,
    "Park Royal": 2.2
  },
  "Park Royal": {
    "Alperton": 2.37,
    "North Ealing": 1.52
  },
  "North Ealing": {
    "Park Royal": 1.67,
    "Ealing Common": 1.65
  },
  "Hammersmith (Dist&Picc Line)": {
    "Turnham Green": 1,
    "Barons Court": 1
  },
  "Knightsbridge": {
    "South Kensington": 2.23,
    "Hyde Park Corner": 1.1
  },
  "Hyde Park Corner": {
    "Knightsbridge": 1.12,
    "Green Park": 1.73
  },
  "Covent Garden": {
    "Leicester Square": 0.77,
    "Holborn": 1.4
  },
  "Russell Square": {
    "Holborn": 1.37,
    "King's Cross St. Pancras": 1
  },
  "Caledonian Road": {
    "King's Cross St. Pancras": 1,
    "Holloway Road": 1.18
  },
  "Holloway Road": {
    "Caledonian Road": 1.2,
    "Arsenal": 1.28
  },
  "Arsenal": {
    "Holloway Road": 1.3,
    "Finsbury Park": 1.38
  },
  "Finsbury Park": {
    "Arsenal": 1.35,
    "Manor House": 1.55,
    "Highbury & Islington": 1,
    "Seven Sisters": 4.25
  },
  "Manor House": {
    "Finsbury Park": 1.67,
    "Turnpike Lane": 2.88
  },
  "Turnpike Lane": {
    "Manor House": 2.87,
    "Wood Green": 1.57
  },
  "Wood Green": {
    "Turnpike Lane": 1.52,
    "Bounds Green": 2.23
  },
  "Bounds Green": {
    "Wood Green": 2.2,
    "Arnos Grove": 2.58
  },
  "Arnos Grove": {
    "Bounds Green": 2.25,
    "Southgate": 2.8
  },
  "Southgate": {
    "Arnos Grove": 3.28,
    "Oakwood": 2.48
  },
  "Oakwood": {
    "Southgate": 2.37,
    "Cockfosters": 2.83
  },
  "Cockfosters": {
    "Oakwood": 2.27
  },
  "Heathrow Terminal 5": {
    "Heathrow Terminals 2 & 3": 1
  },
  "Heathrow Terminals 2 & 3": {
    "Heathrow Terminal 5": 1,
    "Hatton Cross": 1,
    "Heathrow Terminal 4": 1,
    "Hayes & Harlington": 1
  },
  "Hatton Cross": {
    "Heathrow Terminals 2 & 3": 1,
    "Hounslow West": 3.25
  },
  "Hounslow West": {
    "Hatton Cross": 3.3,
    "Hounslow Central": 1.98
  },
  "Hounslow Central": {
    "Hounslow West": 1.85,
    "Hounslow East": 1.3
  },
  "Hounslow East": {
    "Hounslow Central": 1.27,
    "Osterley": 1.53
  },
  "Osterley": {
    "Hounslow East": 1.52,
    "Boston Manor": 2.85
  },
  "Boston Manor": {
    "Osterley": 2.85,
    "Northfields": 1.98
  },
  "Northfields": {
    "Boston Manor": 1.55,
    "South Ealing": 0.98
  },
  "South Ealing": {
    "Northfields": 0.95,
    "Acton Town": 2.93
  },
  "Heathrow Terminal 4": {
    "Heathrow Terminals 2 & 3": 1
  },
  "Brixton": {
    "Stockwell": 2.18
  },
  "Vauxhall": {
    "Stockwell": 2.3,
    "Pimlico": 1.37
  },
  "Pimlico": {
    "Vauxhall": 1.4,
    "Victoria": 2.18
  },
  "Highbury & Islington": {
    "King's Cross St. Pancras": 1,
    "Finsbury Park": 1
  },
  "Seven Sisters": {
    "Finsbury Park": 3.77,
    "Tottenham Hale": 1.6
  },
  "Tottenham Hale": {
    "Seven Sisters": 2.0,
    "Blackhorse Road": 1.97
  },
  "Blackhorse Road": {
    "Tottenham Hale": 1.9,
    "Walthamstow Central": 1
  },
  "Walthamstow Central": {
    "Blackhorse Road": 1
  },
  "Waterloo  ": {
    "Bank": 1
  },
  "Shadwell": {
    "Bank": 1,
    "Limehouse": 1,
    "Tower Gateway": 1
  },
  "Limehouse": {
    "Shadwell": 1,
    "Westferry": 1
  },
  "Westferry": {
    "Limehouse": 1,
    "Canary Wharf": 1,
    "Poplar": 1
  },
  "Heron Quays": {
    "Canary Wharf": 1,
    "South Quay": 1
  },
  "South Quay": {
    "Heron Quays": 1,
    "Crossharbour": 1
  },
  "Crossharbour": {
    "South Quay": 1,
    "Mudchute": 1
  },
  "Mudchute": {
    "Crossharbour": 1,
    "Island Gardens": 1
  },
  "Island Gardens": {
    "Mudchute": 1,
    "Cutty Sark (for Maritime Greenwich)": 1
  },
  "Cutty Sark (for Maritime Greenwich)": {
    "Island Gardens": 1,
    "Greenwich": 1
  },
  "Greenwich": {
    "Cutty Sark (for Maritime Greenwich)": 1,
    "Deptford Bridge": 1
  },
  "Deptford Bridge": {
    "Greenwich": 1,
    "Elverson Road": 1
  },
  "Elverson Road": {
    "Deptford Bridge": 1,
    "Lewisham": 1
  },
  "Lewisham": {
    "Elverson Road": 1
  },
  "Poplar": {
    "Westferry": 1,
    "Blackwall": 1,
    "All Saints": 1,
    "West India Quay": 1
  },
  "Blackwall": {
    "Poplar": 1,
    "East India": 1
  },
  "East India": {
    "Blackwall": 1,
    "Canning Town": 1
  },
  "West Silvertown": {
    "Canning Town": 1,
    "Pontoon Dock": 1
  },
  "Pontoon Dock": {
    "West Silvertown": 1,
    "London City Airport": 1
  },
  "London City Airport": {
    "Pontoon Dock": 1,
    "King George V": 1
  },
  "King George V": {
    "London City Airport": 1,
    "Woolwich Arsenal": 1
  },
  "Woolwich Arsenal": {
    "King George V": 1
  },
  "Pudding Mill Lane": {
    "Stratford": 1,
    "Bow Church": 1
  },
  "Bow Church": {
    "Pudding Mill Lane": 1,
    "Devons Road": 1
  },
  "Devons Road": {
    "Bow Church": 1,
    "Langdon Park": 1
  },
  "Langdon Park": {
    "Devons Road": 1,
    "All Saints": 1
  },
  "All Saints": {
    "Langdon Park": 1,
    "Poplar": 1
  },
  "West India Quay": {
    "Poplar": 1,
    "Canary Wharf": 1
  },
  "Stratford International": {
    "Stratford": 1
  },
  "Stratford High Street": {
    "Stratford": 1,
    "Abbey Road": 1
  },
  "Abbey Road": {
    "Stratford High Street": 1,
    "West Ham": 1
  },
  "Star Lane": {
    "West Ham": 1,
    "Canning Town": 1
  },
  "Tower Gateway": {
    "Shadwell": 1
  },
  "Royal Victoria": {
    "Canning Town": 1,
    "Custom House (for ExCel)": 1
  },
  "Custom House (for ExCel)": {
    "Royal Victoria": 1,
    "Prince Regent": 1
  },
  "Prince Regent": {
    "Custom House (for ExCel)": 1,
    "Royal Albert": 1
  },
  "Royal Albert": {
    "Prince Regent": 1,
    "Beckton Park": 1
  },
  "Beckton Park": {
    "Royal Albert": 1,
    "Cyprus": 1
  },
  "Cyprus": {
    "Beckton Park": 1,
    "Gallions Reach": 1
  },
  "Gallions Reach": {
    "Cyprus": 1,
    "Beckton": 1
  },
  "Beckton": {
    "Gallions Reach": 1
  },
  "Abbey Wood": {
    "Woolwich": 1
  },
  "Woolwich": {
    "Abbey Wood": 1,
    "Custom House": 1
  },
  "Custom House": {
    "Woolwich": 1,
    "Canary Wharf": 1
  },
  "Acton Main Line": {
    "Paddington": 1,
    "Ealing Broadway": 1
  },
  "West Ealing": {
    "Ealing Broadway": 1,
    "Hanwell": 1
  },
  "Hanwell": {
    "West Ealing": 1,
    "Southall": 1
  },
  "Southall": {
    "Hanwell": 1,
    "Hayes & Harlington": 1
  },
  "Hayes & Harlington": {
    "Southall": 1,
    "West Drayton": 1,
    "Heathrow Terminals 2 & 3": 1
  },
  "West Drayton": {
    "Hayes & Harlington": 1,
    "Iver": 1
  },
  "Iver": {
    "West Drayton": 1,
    "Langley": 1
  },
  "Langley": {
    "Iver": 1,
    "Slough": 1
  },
  "Slough": {
    "Langley": 1,
    "Burnham": 1
  },
  "Burnham": {
    "Slough": 1,
    "Taplow": 1
  },
  "Taplow": {
    "Burnham": 1,
    "Maidenhead": 1
  },
  "Maidenhead": {
    "Taplow": 1,
    "Twyford": 1
  },
  "Twyford": {
    "Maidenhead": 1,
    "Reading": 1
  },
  "Reading": {
    "Twyford": 1
  },
  "Shenfield": {
    "Brentwood": 1
  },
  "Brentwood": {
    "Shenfield": 1,
    "Harold Wood": 1
  },
  "Harold Wood": {
    "Brentwood": 1,
    "Gidea Park": 1
  },
  "Gidea Park": {
    "Harold Wood": 1,
    "Romford": 1
  },
  "Romford": {
    "Gidea Park": 1,
    "Chadwell Heath": 1
  },
  "Chadwell Heath": {
    "Romford": 1,
    "Goodmayes": 1
  },
  "Goodmayes": {
    "Chadwell Heath": 1,
    "Seven Kings": 1
  },
  "Seven Kings": {
    "Goodmayes": 1,
    "Ilford": 1
  },
  "Ilford": {
    "Seven Kings": 1,
    "Manor Park": 1
  },
  "Manor Park": {
    "Ilford": 1,
    "Forest Gate": 1
  },
  "Forest Gate": {
    "Manor Park": 1,
    "Maryland": 1
  },
  "Maryland": {
    "Forest Gate": 1,
    "Stratford": 1
  }
}
