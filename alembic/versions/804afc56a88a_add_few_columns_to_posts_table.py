"""add few columns to posts table

Revision ID: 804afc56a88a
Revises: dca672d9bc26
Create Date: 2022-10-31 12:20:29.600377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '804afc56a88a'
down_revision = 'dca672d9bc26'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
    sa.Column('published', sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('posts',
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts','created_at')
    pass
