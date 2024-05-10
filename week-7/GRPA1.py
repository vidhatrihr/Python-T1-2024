def calculate_points(matches):

    points ={}
    
    for match in matches:
        winner = match[0]
        if winner not in points:
            points[winner] = 1
        else:
            points[winner] += 1
        return points
    
    points = {'CSK':0, 'DC':0, 'KKR':0, 'MI':0, 'PK':0, 'RR':0, 'RCB':0, 'SH':0}
    
    
        
