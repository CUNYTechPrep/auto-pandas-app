# Water Sports Equipment Store Sales Data

This directory contains a set of CSV files that simulate sales data for a Shopify-based water sports equipment store. These files can be used for analytics, reporting, and data visualization tasks.

## Files and Schema

### products.csv
Contains information about the products available in the store.
- `product_id`: Unique identifier for each product (e.g., P001)
- `product_name`: Name of the product
- `category`: Main product category (e.g., Surfboards, Wetsuits)
- `subcategory`: More specific product type
- `brand`: Product brand
- `supplier`: Supplier name
- `cost`: Wholesale cost to the store
- `price`: Retail price to customers
- `tags`: Comma-separated tags for the product
- `created_at`: Date when product was added to catalog
- `is_active`: Whether the product is currently active in the catalog

### customers.csv
Contains customer information.
- `customer_id`: Unique identifier for each customer (e.g., C001)
- `first_name`: Customer's first name
- `last_name`: Customer's last name
- `email`: Customer's email address
- `phone`: Customer's phone number
- `address`: Street address
- `city`: City
- `state`: State/province
- `zip`: Postal code
- `country`: Country
- `customer_since`: Date when customer first purchased
- `loyalty_tier`: Customer loyalty program tier (Bronze, Silver, Gold, Platinum)
- `birthdate`: Customer's birth date
- `gender`: Customer's gender (M/F)

### orders.csv
Contains order header information.
- `order_id`: Unique identifier for each order (e.g., O10001)
- `customer_id`: Reference to customer who placed the order
- `order_date`: Date when the order was placed
- `total_amount`: Total order amount (excluding tax, shipping)
- `discount_amount`: Total discount applied to the order
- `shipping_amount`: Shipping cost
- `tax_amount`: Tax amount
- `payment_method`: Method of payment (credit_card, paypal, etc.)
- `shipping_method`: Shipping method (standard, express, etc.)
- `order_status`: Current status of the order
- `promo_code`: Promotional code used (if any)
- `device_type`: Type of device used to place the order
- `store_id`: Store ID (online or physical store ID)

### order_items.csv
Contains line items for each order.
- `order_item_id`: Unique identifier for each order item
- `order_id`: Reference to the order
- `product_id`: Reference to the product
- `quantity`: Quantity ordered
- `price_per_unit`: Price per unit
- `discount_amount`: Discount amount applied to this item
- `total_price`: Total price for this line item (after discounts)
- `is_gift`: Whether this item was marked as a gift

### inventory.csv
Contains inventory information.
- `inventory_id`: Unique identifier for inventory record
- `product_id`: Reference to the product
- `warehouse_id`: Reference to the warehouse
- `stock_quantity`: Current stock quantity
- `restock_level`: Level at which reordering is triggered
- `last_restock_date`: Date of last restocking
- `next_restock_date`: Planned date for next restock
- `shelf_location`: Physical location in warehouse
- `created_at`: Date when inventory record was created
- `updated_at`: Date when inventory record was last updated

### warehouses.csv
Contains warehouse information.
- `warehouse_id`: Unique identifier for each warehouse
- `warehouse_name`: Name of the warehouse
- `address`: Street address
- `city`: City
- `state`: State/province
- `zip`: Postal code
- `country`: Country
- `phone`: Phone number
- `manager_name`: Name of the warehouse manager
- `capacity_sqft`: Warehouse capacity in square feet
- `storage_type`: Type of storage (standard, climate_controlled)
- `shipping_zone`: Geographical shipping zone
- `is_active`: Whether the warehouse is currently active

### marketing_campaigns.csv
Contains marketing campaign information.
- `campaign_id`: Unique identifier for each campaign
- `campaign_name`: Name of the campaign
- `start_date`: Campaign start date
- `end_date`: Campaign end date
- `budget`: Campaign budget
- `platform`: Marketing platform (Email, Social_Media, etc.)
- `target_audience`: Target audience segment
- `discount_code`: Discount code used in the campaign
- `discount_amount`: Discount amount
- `discount_type`: Type of discount (percent, fixed)
- `min_purchase`: Minimum purchase amount required
- `product_category`: Product category targeted
- `clicks`: Number of clicks received
- `impressions`: Number of impressions received
- `conversions`: Number of conversions
- `revenue`: Revenue attributed to the campaign
- `ROI`: Return on investment (percentage)

## Relationships

These tables can be joined using the following relationships:
- orders.customer_id → customers.customer_id
- order_items.order_id → orders.order_id
- order_items.product_id → products.product_id
- inventory.product_id → products.product_id
- inventory.warehouse_id → warehouses.warehouse_id

## Example Analysis Questions

1. What are the best-selling product categories by month?
2. Which customers have the highest lifetime value?
3. How effective are different marketing campaigns at generating revenue?
4. What's the seasonal buying pattern for different product categories?
5. Which products are frequently purchased together?
6. How does inventory turnover differ across product categories?
7. What is the correlation between marketing spend and revenue by product category?
8. How do different shipping methods affect customer reorder rates? 