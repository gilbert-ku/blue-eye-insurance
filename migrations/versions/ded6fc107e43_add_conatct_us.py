"""add conatct us

Revision ID: ded6fc107e43
Revises: 3162b59677b2
Create Date: 2024-03-13 12:11:19.112391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ded6fc107e43'
down_revision = '3162b59677b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('comment', sa.String(length=300), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact')
    # ### end Alembic commands ###
