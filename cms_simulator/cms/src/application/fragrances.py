import random
from cms.src.domain.models.fragrance import Fragrance
from cms.src.infrastructure.logging import logger


def modify_fragrance(db):

    should_change = lambda: random.choice([True,False])
    fragrance_to_update = random.choice(db.query(Fragrance).all())

    old_name = fragrance_to_update.name
    logger.info(f"Updating fragance {fragrance_to_update.fragrance_id} ")
    
    delta_changes = {
        "fragrance_id": fragrance_to_update.fragrance_id
    }

    if should_change():
        new_name = old_name + "HOOOOOOOOOOLAAA"
        logger.info(f"New name {new_name}")

        delta_changes["name"] = new_name
        fragrance_to_update.name = new_name
        
    if should_change:
        new_description = fragrance_to_update.description + "blabla..."
        logger.info(f"New forbidden state {not fragrance_to_update.forbidden}")

        delta_changes["description"] = new_description
        fragrance_to_update.description = new_description

    if should_change:
        new_forbidden = not fragrance_to_update.forbidden
        logger.info(f"New forbidden state {not fragrance_to_update.forbidden}")

        delta_changes["forbidden"] = new_forbidden
        fragrance_to_update.forbidden = new_forbidden

    new_val = random.randint(0,10)
    if  new_val >=5:
        new_cost = int(fragrance_to_update.cost) + new_val
        logger.info(f"New cost {new_cost}")

        delta_changes["cost"] = new_cost
        fragrance_to_update.cost = new_cost

    db.commit()
    db.flush()
    db.close()

    return delta_changes