"""create posts table

Revision ID: 73e515422f64
Revises: 
Create Date: 2022-10-30 22:22:32.956412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73e515422f64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
