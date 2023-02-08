def get_frame_Cu(i, num_Si, num_atoms, lines):
    
    Cu_data = []
    for j in range((i*(num_atoms+2))+num_Si+2,((i)*(num_atoms+2))+num_atoms+2):
        Cu_data.append(lines[j].split())
        
    return Cu_data
