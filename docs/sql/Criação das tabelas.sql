CREATE TABLE cpu
(
	id INTEGER NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    cores INTEGER NOT NULL,
	base_clock VARCHAR(50) NOT NULL,
    boost_clock VARCHAR(50) NULL,
    integrated_graphics VARCHAR(50) NULL,
    multithreading INTEGER NOT NULL,
    price DOUBLE NOT NULL, 
    PRIMARY KEY(id)
);

CREATE TABLE gpu
(
	id INTEGER NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    chipset VARCHAR(50) NOT NULL,
    base_clock VARCHAR(50) NOT NULL,
    boost_clock VARCHAR(50) NULL,
    color VARCHAR(50) NOT NULL,
    length FLOAT NOT NULL,
    price DOUBLE NULL,
    PRIMARY KEY(id)
);

CREATE TABLE motherboard
(
	id INTEGER NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    socket_ VARCHAR(50) NOT NULL,
    form_factor VARCHAR(50) NOT NULL,
    ram_slots INTEGER NOT NULL,
    max_ram VARCHAR(50) NOT NULL,
    color VARCHAR(50) NULL,
    price DOUBLE NULL,
    PRIMARY KEY(id)
);

CREATE TABLE build
(
	id INTEGER NOT NULL,
    cpu_id INTEGER NOT NULL,
    gpu_id INTEGER NOT NULL,
    motherboard_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(cpu_id) REFERENCES cpu(id),
    FOREIGN KEY(gpu_id) REFERENCES gpu(id),
    FOREIGN KEY(motherboard_id) REFERENCES motherboard(id)
);

SELECT * FROM cpu;
SELECT * FROM gpu;
SELECT * FROM motherboard;