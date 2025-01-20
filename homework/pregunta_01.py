"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
        
    import pandas as pd

    # Leer el contenido del archivo
    with open('./files/input/clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Procesar las líneas para construir el DataFrame
    data = []
    cluster = None
    cantidad_palabras_clave = None
    porcentaje_palabras_clave = None
    principales_palabras_clave = []

    for line in lines[4:]:
        if line.strip():
            if line.lstrip()[0].isdigit():
                if cluster is not None:
                    data.append([cluster, cantidad_palabras_clave, porcentaje_palabras_clave, ', '.join(principales_palabras_clave)])
                parts = line.split(maxsplit=3)
                cluster = int(parts[0])
                cantidad_palabras_clave = int(parts[1])
                porcentaje_palabras_clave = float(parts[2].replace(',', '.').replace('%', ''))
                principales_palabras_clave = [parts[3].strip()]
            else:
                principales_palabras_clave.append(line.strip())

    # Añadir el último cluster
    if cluster is not None:
        data.append([cluster, cantidad_palabras_clave, porcentaje_palabras_clave, ', '.join(principales_palabras_clave)])

    # Crear el DataFrame
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    df

    # Limpiar las palabras clave
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace(r'\s+', ' ', regex=True).str.replace(r',\s+', ', ').str.replace(',,' , ',')
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str[2:]
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: x + ".")

    df.at[0,'principales_palabras_clave'] = "maximum power point tracking, fuzzy-logic based control, photo voltaic (pv), photo-voltaic system, differential evolution algorithm, evolutionary algorithm, double-fed induction generator (dfig), ant colony optimisation, photo voltaic array, firefly algorithm, partial shade"
    df.at[1,'principales_palabras_clave'] =(
        "support vector machine, "
        "long short-term memory, "
        "back-propagation neural network, "
        "convolution neural network, "
        "speed wind prediction, "
        "energy consumption, "
        "wind power forecasting, "
        "extreme learning machine, "
        "recurrent-neural-network (rnn), "
        "radial basis "
        "function (rbf) networks, "
        "wind farm"
    )
    df.at[2,'principales_palabras_clave'] =(
        "smart grid, "
        "wind power, "
        "reinforcement learning, "
        "energy management, "
        "energy efficiency, "
        "solar energy, "
        "deep reinforcement learning, "
        "demand-response (dr), "
        "internet of things, "
        "energy harvester, "
        "q-learning"
    )
    df.at[3,'principales_palabras_clave'] =(
        "wind turbine, "
        "fault diagnosis, "
        "biodiesel, "
        "failure detection, "
        "response-surface methodology, "
        "condition monitoring, "
        "load forecasting, "
        "energy consumption forecast, "
        "anomalies detection, "
        "optimization-based algorithm, "
        "supervisory control and data acquisition"
    )
    df.at[4,'principales_palabras_clave'] =(
        "electric vehicle, "
        "lithium-ion batteries, "
        "state of charge, "
        "state of health, "
        "hybrid-electric vehicle, "
        "energy management strategies, "
        "energy management system, "
        "remaining useful life, "
        "battery management system, "
        "transfer learning, "
        "hybrid energy storage"
    )
    df.at[5,'principales_palabras_clave'] =(
        "particle swarm optimization, "
        "distribute generation, "
        "solar irradiance, "
        "artificial bee colonies, "
        "energy storage systems, "
        "bat algorithm, "
        "gravitational search algorithm, "
        "distributed system, "
        "multi-objective swarm optimization (mopso), "
        "optimal power-flow (opf), "
        "load-frequency control"
    )
    df.at[6,'principales_palabras_clave'] =(
        "multi-objective optimization, "
        "energy storage, "
        "economic dispatch, "
        "non-dominated sorting genetic algorithm, "
        "sensitive analysis, "
        "hybrid renewable energy source, "
        "plug-in electric vehicle, "
        "combined-heat and power, "
        "multi-objective genetic algorithm, "
        "unit-commitment, "
        "dc-dc converters"
    )
    df.at[7,'principales_palabras_clave'] =(
        "genetic algorithm, "
        "demand-side management, "
        "energy-saving, "
        "hybrid electric system (hes), "
        "wind turbine blade, "
        "data-driven modelling, "
        "simulated annealing, "
        "solar forecasting, "
        "geographic information system, "
        "renewable energy system, "
        "cogeneration"
    )
    df.at[8,'principales_palabras_clave'] =(
        "anfis, "
        "global solar irradiance, "
        "solar irradiance forecast, "
        "genetic programing, "
        "islanding detection, "
        "expert system, "
        "distributed networks, "
        "evolutionary computation, "
        "wavelet-based neural network, "
        "root mean square errors, "
        "virtual power plant"
    )
    df.at[9,'principales_palabras_clave'] =(
        "micro grid, "
        "multi-agent systems, "
        "distributed energy resource, "
        "batteries energy storage system, "
        "dc micro grid, "
        "pitch-control, "
        "droop control, "
        "hybrid ac/dc microgrid, "
        "voltage regulation, "
        "superconducting magnetic energy storage, "
        "distributed-control"
    )
    df.at[10,'principales_palabras_clave'] =(
        "hydrogen, "
        "biochar, "
        "biomass, "
        "biogas, "
        "microbial fuel cell, "
        "gasification, "
        "biofuel, "
        "ethanol, "
        "engine performance, pyrolysis, "
        "anaerobic digester"
    )
    df.at[11,'principales_palabras_clave'] =(
        "state of charge (soc) estimation, "
        "radial basis function, "
        "short-term load forecasting, "
        "computational fluid dynamics, "
        "generalized-regression neural network, "
        "monte-carlo simulation, "
        "multiple linear regression, "
        "power generation, "
        "nonlinear auto-regressive exogenous (narx) model neural "
        "networks, "
        "surrogate model, "
        "extreme gradient boosting"
    )
    df.at[12,'principales_palabras_clave'] =(
        "pem fuel cell, "
        "solid-oxide fuel cell, "
        "deep-belief networks, "
        "energy optimisation, "
        "particles-size distributions, "
        "biomass gasification, "
        "exergy, "
        "battery management, "
        "hydrogen production, "
        "numeric simulation, "
        "system-identification"
    )
    
    return df

    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
