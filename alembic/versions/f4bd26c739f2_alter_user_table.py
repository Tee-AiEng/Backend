"""alter user table

Revision ID: f4bd26c739f2
Revises: 
Create Date: 2025-10-23 11:18:19.930099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4bd26c739f2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
    ALTER TABLE user
    ADD COLUMN usertype varchar(100) DEFAULT "student"
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
    ALTER TABLE user
    DROP COLUMN usertype 
""")
    pass
