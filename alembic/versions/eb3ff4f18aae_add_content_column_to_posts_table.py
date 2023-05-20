"""add content column to posts table

Revision ID: eb3ff4f18aae
Revises: 51d7d5f8fe05
Create Date: 2023-05-18 18:42:39.084097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb3ff4f18aae'
down_revision = '51d7d5f8fe05'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

    pass


def downgrade():
    op.drop_column('posts','content')

    pass
