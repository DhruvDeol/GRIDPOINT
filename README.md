# GRIDPOINT
An intelligent warehouse location optimization system that minimizes delivery costs by analyzing neighborhood coordinates, order demand, and warehouse assignments.
## PROBLEM
- Warehouse location optimization based on neighborhood demand and delivery distance.

## OUR SOLUTION
- We calculated weighted delivery cost and identify warehouse locations that minimize overall delivery cost.

## TECHNOLOGIES AND LIBRARIES
1. Python - Backend
2. Streamlit - Web Interface
3. Pandas - Data Handling
4. Git and Github - Version Control

## HOW TO RUN
```terminal
pip install -r requirements.txt
streamlit run app.py
```
## MATH USED

### 1. Euclidean Distance

The distance between warehouse \(w\) and neighborhood \(i\) is calculated as:

$$
d_{wi} = \sqrt{(x_i-x_w)^2 + (y_i-y_w)^2}
$$

where:

- $$\(x_i, y_i\)$$ = coordinates of neighborhood \(i\)
- $$\(x_w, y_w\)$$ = coordinates of warehouse \(w\)
- $$\(d_{wi}\)$$ = distance between warehouse \(w\) and neighborhood \(i\)

### 2. Order-Weighted Delivery Cost

The delivery cost for neighborhood \(i\) is:

$$
C_i = D_i \times d_{w(i),i}
$$

where:

- $\(D_i\)$ = number of orders at neighborhood \(i\)
- $$\(d_{w(i),i}\)$$ = distance between neighborhood \(i\) and its assigned warehouse

### 3. Objective Function

The objective of GRIDPOINT is to minimize the total delivery cost:

$$
\boxed{
\min C = \sum_{i=1}^{N} D_i \times d_{w(i),i}
}
$$

where:

- $$\(N\)$$ = total number of neighborhoods
- $$\(D_i\)$$ = order demand at neighborhood \(i\)
- $$\(w(i)\)$$ = warehouse assigned to neighborhood \(i\)
- $$\(d_{w(i),i}\)$$ = distance from the assigned warehouse to neighborhood \(i\)

### 4. Assignment Constraint

Every neighborhood must be assigned to exactly one warehouse:

$$
\sum_{w=1}^{K} x_{wi} = 1
\quad \forall i
$$

where:

- $$\(K\)$$ = number of warehouses
- $$\(x_{wi}=1\)$$ if neighborhood \(i\) is assigned to warehouse \(w\)
- $$\(x_{wi}=0\)$$ otherwise

### 5. Warehouse Selection

For the current prototype, warehouse locations are selected from the available neighborhood locations.

The algorithm evaluates possible warehouse combinations and selects the configuration with the minimum total order-weighted delivery distance.

## TEAM
1. Atheeth Ram KM
2. Dhruv Deol
3. Hemant
4. Rudra Mittal

## REFERENCES

ChatGPT was used as an AI-assisted development tool during the creation of this project.

It helped the team with:
- Generating and explaining Python code
- Developing the optimization algorithm
- Debugging and resolving coding errors
- Designing parts of the Streamlit interface
- Improving project documentation

The generated code was reviewed, tested, modified, and integrated by the team according to the requirements of the GRIDPOINT project.
