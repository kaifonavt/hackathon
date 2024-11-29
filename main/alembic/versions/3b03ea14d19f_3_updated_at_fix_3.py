"""3 Updated at fix 3

Revision ID: 3b03ea14d19f
Revises: 0a5d145ad057
Create Date: 2024-11-29 23:07:26.508350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b03ea14d19f'
down_revision: Union[str, None] = '0a5d145ad057'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('activity_logs', 'updated_at')
    op.add_column('activity_logs', sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    


def downgrade() -> None:
    pass
