"""init migrations 

Revision ID: e564293e0a98
Revises: 
Create Date: 2022-02-14 09:09:29.748611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e564293e0a98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_email', sa.String(length=255), nullable=True),
    sa.Column('usernane', sa.String(length=255), nullable=True),
    sa.Column('login_password', sa.String(length=255), nullable=True),
    sa.Column('profile_img_path', sa.String(), nullable=True),
    sa.Column('joined_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_user_email'), 'users', ['user_email'], unique=True)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_title', sa.String(), nullable=True),
    sa.Column('post_description', sa.Text(), nullable=True),
    sa.Column('auther_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['auther_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_post_description'), 'posts', ['post_description'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_descrip', sa.Text(), nullable=True),
    sa.Column('time_posted', sa.DateTime(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_time_posted'), 'comments', ['time_posted'], unique=False)
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('like', sa.Integer(), nullable=True),
    sa.Column('post_like_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_like_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unlikes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unlike', sa.Integer(), nullable=True),
    sa.Column('post_unlike_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_unlike_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('unlikes')
    op.drop_table('likes')
    op.drop_index(op.f('ix_comments_time_posted'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_posts_post_description'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_users_user_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###