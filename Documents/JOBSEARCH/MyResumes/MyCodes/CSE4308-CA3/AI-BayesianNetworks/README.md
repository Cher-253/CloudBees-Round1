## Probability Networks   
### Bayesian Network and Candy Bag Probability  

This project consists of two Python scripts, each addressing different probabilistic scenarios.  

Task 1: Bayesian Network (bnet.py)  
This script implements a Bayesian network to calculate conditional probabilities based on given information. The Bayesian network has nodes representing boolean variables (B, E, A, J, M) and conditional probability values associated with each node. The bayesianNetwork class defines these probabilities, and the computeProbability method calculates the joint probability based on input values.  

Usage:  
bash```
python3 bnet.py Bf At Mt  
```  
Replace the arguments (e.g., Bf At Mt) with the desired boolean values for the variables B, A, and M.  

Notes:  
Joint Probability: e.g., Bf At Mt  
Conditional Probability: e.g., Jt given Et Bf  
Marginal Probability: e.g., Jf Mt given Et  


Task 2: Candy Bag Probability (posteriorprobability.py)  
This script models the probability of picking candies from different bags based on observations. The bags class defines bags with prior probabilities and probabilities of picking cherry or lime candies from each bag. The script updates probabilities based on observations and calculates posterior probabilities.  

Usage:  
bash```
python3 posteriorprobability.py LCCCCCCCCCCCLLLLLLLLLLLLLLLLLLLLLLL
```  
Replace the argument (e.g., LCCCCCCCCC...) with the observed candy sequence.  

Notes:  
The script outputs the probabilities of picking cherry and lime candies after each observation.  
