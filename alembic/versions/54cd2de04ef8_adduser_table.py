"""adduser table

Revision ID: 54cd2de04ef8
Revises: 68d2b8b11f0f
Create Date: 2022-10-31 12:01:53.921089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54cd2de04ef8'
down_revision = '68d2b8b11f0f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('email',sa.String(),nullable=False),
    sa.Column('password',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),
    server_default=sa.text('now()'),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
