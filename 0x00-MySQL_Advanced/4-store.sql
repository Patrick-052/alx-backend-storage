-- a trigger that decrease quantity of an item after an order

CREATE TRIGGER `trigger_update_quantity`
AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;

