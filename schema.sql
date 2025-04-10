-- test_project/schema.sql

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INT,
    name VARCHAR(100) NOT NULL,
    description TEXT NULL,
    price DECIMAL(10, 2),
    -- Inline PK constraint
    PRIMARY KEY (product_id)
);

-- Table with composite primary key and foreign key
CREATE TABLE orders (
    order_id INT NOT NULL,
    order_date DATE,
    customer_id INT, -- FK column
    CONSTRAINT pk_orders PRIMARY KEY (order_id), -- Table level PK
    CONSTRAINT fk_orders_users FOREIGN KEY (customer_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Table with multi-column foreign key
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT DEFAULT 1,
    -- Table level constraints
    PRIMARY KEY (order_id, product_id), -- Composite PK
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
    -- Missing ON DELETE for product FK deliberately
);

-- Example of a table without explicit PK (might happen)
CREATE TABLE logs (
    log_id INT AUTO_INCREMENT, -- Type might vary, parser handles as string
    message TEXT,
    log_time TIMESTAMP
);

-- Example of index (parser currently ignores this)
CREATE INDEX idx_username ON users(username);