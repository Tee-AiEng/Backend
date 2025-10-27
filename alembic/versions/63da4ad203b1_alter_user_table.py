"""alter user table

Revision ID: 63da4ad203b1
Revises: f4bd26c739f2
Create Date: 2025-10-27 11:05:48.427421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63da4ad203b1'
down_revision: Union[str, Sequence[str], None] = 'f4bd26c739f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
    ALTER TABLE user
    ADD COLUMN gender varchar(100) DEFAULT "male"
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
    ALTER TABLE user
    DROP COLUMN gender 
""")
    pass
