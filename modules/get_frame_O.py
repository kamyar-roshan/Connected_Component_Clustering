def get_frame_O(i, num_Si, num_atoms, lines):
    
    O_data = []
    for j in range((i*(num_atoms+2))+num_Si+16,((i)*(num_atoms+2))+num_atoms+2):
        O_data.append(lines[j].split())
        
    return O_data
