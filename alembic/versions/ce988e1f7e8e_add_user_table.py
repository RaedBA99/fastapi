"""add user table

Revision ID: ce988e1f7e8e
Revises: eb3ff4f18aae
Create Date: 2023-05-18 19:57:16.662770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce988e1f7e8e'
down_revision = 'eb3ff4f18aae'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('pasword', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')          
                    )


    pass


def downgrade():
    op.drop_table('users')
    pass
