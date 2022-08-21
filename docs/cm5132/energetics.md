# Chemical Energetics


## Summary (for those in a hurry)
- $U = q - w = n \Delta H - p \Delta V = -(mc+C)\Delta T-p\Delta V$
- Standard State ($H^{\circ}$) is 1M for aqueous, 1 atm for gaseous and pure otherwise

|Name|Symbol|Definition|
|---|---|--------------|
|Formation Enthalpy|$\Delta H_f$|Enthalpy change to form one mole of molecule|
|Combustion Enthalpy|$\Delta H_c$|Enthalpy change to combust one mole of molecule|
|Neutralisation Enthalpy|$\Delta H_n$|Enthalpy change to form one mole of water in neutralisation|
|Atomization Enthalpy|$\Delta H_a$|Enthalpy change to form one mole of element for uni-elemental or to react one mole of molecule for multi-elemental molecules|
|Bond Energy|$BE$|Energy required to break one mole of said bond|
|Lattice Energy|$\Delta H_{LE}$|Energy required to dissociated an ionic lattice into gaseous ions|
|$n$th Ionization Energy|$\Delta H_{IE, n}$|Energy required for element to release $n$th electron|
|$n$th Electron Affinity|$\Delta H_{EA, n}$|Energy required for element to accept $n$th electron|
|Hydration Enthalpy|$\Delta H_{hyd}$|Energy required to dissolve gaseous ions into water|
|Solution Enthalpy|$\Delta H_{sol}$|Energy required to dissolve anything into water|

## First Law of Thermodynamics
$$
\begin{align*}
\Delta U &= q - w  \\
&= n \Delta H - p \Delta V
\end{align*}
$$

Where $\Delta U$ is the change in internal energy of the system, $q$ is the heat absorbed by the system and $w$ is the work done by the system. $\Delta H$ is the enthalpy change of a given reaction within the system, $p$ is the pressure exerted, $\Delta V$ is the change in volume of the system.


## Enthalpy, $\Delta H$
Essentially change in heat of system caused by any particular reaction taking place within said system.

It is a **state function**, which means every path to get from one set of reactants to one set of products requires the same enthalpy change. This also means that the reverse reaction has the opposite polarity and same magnitude of enthalpy change.

### Standard State Enthalpy, $\Delta H ^{\circ}$

Enthalpy change is not the same at every point. Different variables like temperature, pressure and concentration and more can influence the enthalpy change. Standard State is defined to be the following:

|State|Condition for Standard State Enthalpy|
|----|--------------|
|Liquid, Solid|Pure|
|Gaseous|1 atm|
|Aqueous|1 M|

### Computing $\Delta H$ experimentally

In most reactions, we often conduct it in water, or on a surface not participating in the reaction (or both, like in a Calorimeter). In this case, we must know the following values:

- Specific Heat Capacity of the **Solution**: $c$
- Mass of the **Solution**: $m$
- Heat Capacity of Surface: $C$
- Change in Temperature: $\Delta T$

From here, we can compute the energy absorbed/supplied by the surroundings via the formula $q = mc\Delta T + C\Delta T$. This is the energy released for the given moles of reactants, so we need to divide it by said number of moles reacted to get the actual Enthalpy Change. Thus:

$$\Delta H = -\frac{mc\Delta T + C\Delta T}{n_\text{limit}}$$

## Enthalpy of Formation, $\Delta H_f$

Formation Enthalpy is the enthalpy of the reaction that forms the compound from its constituent elements. Note that these elements should be in their most stable allotropic state, which essentially means the state they are most likely to be found in. For a compound $\text{ABC}$, where $\text{A}$ exists in the form of gaseous $\text{A}_2$ for stability, $\text{B}$ remains in solid state and $C$ is Carbon, we have the following expression:

$$\frac{1}{2}\text{ A}_2\text{ (g) } + \text{ B (s) } + \text{ C (graphite)} \rightarrow \text{ABC}\quad\quad\Delta H_f$$

### Using $\Delta H_f$ meaningfully
An extension of this is seen when we are required to compute the enthalpy change of any given reaction. Since we can simplify all reactants to the their allotropic elements via the reverse reaction, and produce the products from said allotropes, we can essentially represent the the reaction enthalpy as follows:

$$\Delta H_{rxn} = \sum n_\text{product} \Delta H_{f, \text{ product}} - \sum n_\text{ reactant} \Delta H_{f, \text{reactant}}$$

This makes it easier for us to retrieve the enthalpy change of a reaction.

## Enthalpy of Combustion, $\Delta H_c$

Combustion is **ALWAYS** an exothermic reaction, so this enthalpy is always negative. The general reaction is as follows:

$$\text{C}_x\text{H}_y\text{O}_z+\frac{4x+y-2z}{4}\text{ O}_2\text{ (g) } \rightarrow x \text{ CO}_2 + \frac{y}{2}\text{ H}_2\text{O}\quad\Delta H_c$$

## Enthalpy of Neutralisation, $\Delta H_n$

This is the enthalpy change of any given neutralisation reaction to form one mole of water.

$$\text{H}^+\text{ (aq)}+\text{OH}^-\text{ (aq)}\rightarrow \text{H}_2\text{O (l)} \quad\quad\Delta H_n$$

**Note:** The above reaction is simply the ionic reaction, this is actually still the enthalpy change of the actual reaction.

## Enthalpy of Atomization, $\Delta H_a$

Atomization has two cases, as follows:

### $\Delta H_a$ for uni-elemental molecules

This pertain to the atomization enthalpy of any given molecule, and the reaction is such that one mole of the **elemental gas** is formed:

$$\frac{1}{n}\text{ X}_n \rightarrow \text{X (g)}\quad\quad\Delta H_a$$

### $\Delta H_a$ for multi-elemental molecules

If any given molecule is made of more that a single elemnt, the reaction is such that one mole of the **molecule** is formed.

$$\text{X}_m\text{Y}_n \rightarrow m\text{ X (g) }+n\text{ Y (g)}\quad\quad\Delta H_a$$

### Using $\Delta H_a$ meaningfully
Same thing as with $\Delta H_f$.

$$\Delta H_{rxn} = \sum n_\text{reactant} \Delta H_{a, \text{ reactant}} - \sum n_\text{product} \Delta H_{a, \text{ product}}$$


## Bond Energy, $BE$

This is technically a side-tour. Bond Energy is the energy required to overcome a bond (i.e it is endothermic, positive). The reaction for an example is as follows:

$$\text{Cl}-\text{Cl} \rightarrow 2\text{ Cl}\quad \quad BE_{\text{Cl}-\text{Cl}}$$

This is similar to the formation enthalpy (of course it's the reverse reaction), 
