import React from 'react';
import { Card as CustomCard } from 'react-bootstrap';
import styles from './Card.module.css';

interface ProfileCardProps {
  ownerUsername: string;
  name: string;
  profilePictureUrl: string;
  bio: string;
  website: string;
}

const ProfileCard: React.FC<ProfileCardProps> = ({
  ownerUsername,
  name,
  profilePictureUrl,
  bio,
  website,
}) => {
  return (
    <CustomCard className={styles.profileCard}>
      <CustomCard.Img
        variant="top"
        className="rounded-circle"
        src={profilePictureUrl}
        alt={`${ownerUsername}'s profile picture`}
      />
      <CustomCard.Body>
        <CustomCard.Title>{name || ownerUsername}</CustomCard.Title>
        <CustomCard.Text>{bio}</CustomCard.Text>
        {website && (
          <CustomCard.Link
            href={website}
            target="_blank"
            rel="noopener noreferrer"
          >
            {website}
          </CustomCard.Link>
        )}
      </CustomCard.Body>
    </CustomCard>
  );
};

export default ProfileCard;
