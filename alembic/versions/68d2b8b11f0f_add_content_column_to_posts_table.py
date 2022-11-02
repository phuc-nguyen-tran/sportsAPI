"""add content column to posts table

Revision ID: 68d2b8b11f0f
Revises: 73e515422f64
Create Date: 2022-10-31 11:57:27.460158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68d2b8b11f0f'
down_revision = '73e515422f64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
